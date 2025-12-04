#1. Setup
import streamlit as st
from backend import MultilingualChatbot
from datetime import datetime

st.title(" Multilingual Chatbot")

if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.all_chats[st.session_state.current_chat_id] = []

#2. Sidebar
with st.sidebar:
    language = st.selectbox("Language", [
        "English", "Spanish", "French", "German",
        "Hindi", "Japanese", "Odia", "Arabic"
    ])
    if st.button("➕New Chat"):
        st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.all_chats[st.session_state.current_chat_id] = []
        st.rerun()
        
    st.markdown("## Previous Chats💬")
    st.markdown("---")
    
    for chat_id in reversed(list(st.session_state.all_chats.keys())):
        chat_messages = st.session_state.all_chats[chat_id]
        if chat_messages:
            first_msg = chat_messages[0]['content'][:30]
            is_current = chat_id == st.session_state.current_chat_id
            
            if st.button(
                f"{'➡️ ' if is_current else '💬'}{first_msg}...",
                key=chat_id,
                use_container_width=True
            ):
                st.session_state.current_chat_id = chat_id
                st.rerun()

#3. Main Area
current_messages = st.session_state.all_chats[st.session_state.current_chat_id]
for msg in current_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Type your message here..."):
    # Display user message
    current_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get response from chatbot
    chatbot = MultilingualChatbot()
    response = chatbot.chat(
        message=prompt,
        language=language,
        history=current_messages
    )
    
    # Display bot response
    current_messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
    
    st.session_state.all_chats[st.session_state.current_chat_id] = current_messages
    st.rerun()