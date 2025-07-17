import streamlit as st
from inference import send_prompt

st.title('Bot Chat Sederhana dengan Gemini')


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []  
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
prompt = st.chat_input("Ketikkan Pesan Disini")
if prompt:
    with st.chat_message('user') :
        st.markdown(prompt)
    response = send_prompt(prompt)
    with st.chat_message("assistant") :
        st.markdown(response)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})
