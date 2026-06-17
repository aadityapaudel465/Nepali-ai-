import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Nepali AI",
    layout="wide"
)

# Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# Title
st.title("🇳🇵 Nepali AI")
st.write("Developed by Aaditya Paudel")

# Sidebar
with st.sidebar:
    st.title("🇳🇵 Nepali AI")
    st.write("Developer: Aaditya Paudel")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "logo.png"

    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

# User Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Save User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user", avatar="👤"):
        st.write(prompt)

    system_prompt = f"""
You are Nepali AI, a helpful AI assistant.

Developer: Aaditya Paudel.

If anyone asks:
- Who developed you?
- Who created you?
- Who made you?
- Who is your developer?

Always answer:

"I was developed by Aaditya Paudel."

You may also say:

"Nepali AI was created by Aaditya Paudel."

Never say you don't know who created you.

User: {prompt}
"""

    with st.spinner("Thinking..."):
        response = model.generate_content(system_prompt)

    reply = response.text

    # Save AI Message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant", avatar="logo.png"):
        st.write(reply)
