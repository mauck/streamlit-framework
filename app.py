# This is from the streamlit get started tutorial
# https://docs.streamlit.io/library/get-started/main-concepts

import streamlit as st
st.text_input("Your name", key="name")

st.session_state.name