import streamlit as st
import google.generativeai as genai

# Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page title
st.image("logo.png", width=200)

st.title("🤖 Nepali AI")

st.write("👨‍💻 Developed by Aaditya Paudel")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt and prompt.strip():

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    system_prompt = f"""
    You are Nepali AI.

    User Message:
    {prompt}
    """

    response = model.generate_content(system_prompt)

    reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    )

    with st.chat_message("assistant"):
        st.write(reply)
    
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

You can also mention:
"Nepali AI was created by Aaditya Paudel."

Never say you don't know who created you.

User: {prompt}
"""

    response = model.generate_content(system_prompt)
    reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)
        st.set_page_config(
    page_title="Nepali AI",
    page_icon="",
    layout="wide")
        st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}

h1 {
    color: #00D4FF;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
with st.sidebar:
    st.title("🇳🇵 Nepali AI")
    st.write("Developer: Aaditya Paudel")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
