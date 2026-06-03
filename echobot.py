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

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user", avatar="🧑").markdown(prompt)
    st.caption("**Human**") 
    

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response)
        st.caption("**Skynet**") 
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




# with st.chat_message("assistant", avatar="🤖"):
    # Displays the name in a small, muted font right inside the bubble
    # st.caption("**Skynet**") 
    # st.write("Are you John Connor?")

# prompt = st.chat_input("Say something")
# if prompt:
    # with st.chat_message("user", avatar="🧑"):
        # Displays the name in a small, muted font right inside the bubble
        # st.caption("**Human**") 
        # st.write(prompt)
