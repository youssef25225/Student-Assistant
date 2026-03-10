import streamlit as st
from groq import Groq

st.title("Study Assistant")

t1, t2, t3 = st.tabs(["Chat", "Quiz", "Flashcards"])

with t1:
    st.header("Chat")

    col1, col2 = st.columns(2)

    with col1:
        subject = st.selectbox("Select Subject", ["Math", "Programming", "Physics", "Chemistry"])
        tone = st.selectbox("Select Tone", ["Casual", "Formal", "Humorous"])

    with col2:
        details = st.selectbox("Select Details", ["Summary", "Explanation", "Examples"])
        edu_level = st.selectbox("Select Education Level", ["High School", "Undergraduate", "Postgraduate"])

    st.divider()

    topic = st.chat_input("Enter Topic")

    if topic:
        with st.chat_message("user"):
            st.write(topic)

        client = Groq(api_key=st.secrets["api"])

        prompt = f"""
        Explain {topic}

        Subject: {subject}
        Tone: {tone}
        Detail level: {details}
        Education level: {edu_level}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        with st.chat_message("assistant"):
            st.write(response.choices[0].message.content)