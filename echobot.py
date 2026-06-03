import streamlit as st
import numpy as np

with st.chat_message("assistant", avatar="🤖"):
    # Displays the name in a small, muted font right inside the bubble
    st.caption("**Skynet**") 
    st.write("Are you John Connor?")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
