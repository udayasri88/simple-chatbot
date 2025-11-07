import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖", layout="centered")

# --- Chatbot logic ---
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! 👋 How can I help you today?"
    elif "your name" in user_input:
        return "I'm PyBot — a friendly Streamlit chatbot!"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking 😄"
    elif "bye" in user_input:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Hmm... I’m not sure I understood that. Could you rephrase?"

# --- Streamlit UI ---
st.title("💬 Simple Chatbot")
st.markdown("Type your message below and chat with PyBot!")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input field
user_input = st.text_input("You:")

# When user clicks Send
if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.session_state.history.append(("🧑 You", user_input))
        st.session_state.history.append(("🤖 PyBot", response))
        st.rerun()  # new method to refresh UI safely

# Display chat history
for sender, message in st.session_state.history:
    st.markdown(f"**{sender}:** {message}")

