import streamlit as st

st.set_page_config(page_title="Nepali AI", page_icon="🤖")

st.title("🤖 Nepali AI")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Temporary AI response
    response = f"You said: {prompt}"

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)