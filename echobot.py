import streamlit as st
import numpy as np

st.title("Echo Bot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []



# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])






with st.chat_message("assistant", avatar="🤖"):
    # Displays the name in a small, muted font right inside the bubble
    st.caption("**Skynet**") 
    st.write("Are you John Connor?")

prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user", avatar="🧑"):
        # Displays the name in a small, muted font right inside the bubble
        st.caption("**Human**") 
        st.write(prompt)
