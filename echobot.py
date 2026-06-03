import streamlit as st
import numpy as np

with st.chat_message("Cyberdyne Systems Model 101"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))
