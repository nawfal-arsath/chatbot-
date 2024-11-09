import streamlit as st
import requests
from streamlit_chat import message

def main():
    st.set_page_config(
        page_title="Chatbot  🤖",
        page_icon=":robot_face:",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    st.title("DialoGPT Chatbot")
    st.sidebar.title("About")
    st.sidebar.info(
        "This is an AI chatbot powered by the DialoGPT model from Hugging Face. "
        "It can engage in open-ended conversations on a variety of topics."
    )

    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_area("Enter your message:", height=100)
        submit_button = st.form_submit_button(label="Send")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if submit_button:
        chat_request = {"prompt": user_input, "history": st.session_state.chat_history}
        response = requests.post("http://localhost:8000/chat/", json=chat_request)
        response.raise_for_status()
        bot_response = response.json()["response"]
        st.session_state.chat_history.append(user_input)
        st.session_state.chat_history.append(bot_response)

    if st.session_state.chat_history:
        st.title("Conversation")
        for i, (user_msg, bot_msg) in enumerate(zip(st.session_state.chat_history[::2], st.session_state.chat_history[1::2])):
            with st.container():
                if i % 2 == 0:
                    message(user_msg, is_user=True, avatar_style="bottts", key=f"user_{i}")
                    message(bot_msg, is_user=False, avatar_style="bottts", key=f"bot_{i}")
                else:
                    message(bot_msg, is_user=False, avatar_style="bottts", key=f"bot_{i}")
                    message(user_msg, is_user=True, avatar_style="bottts", key=f"user_{i}")

if __name__ == "__main__":
    main()