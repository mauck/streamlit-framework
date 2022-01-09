# This is from the streamlit get started tutorial
# https://docs.streamlit.io/library/get-started/main-concepts

import streamlit as st
x = st.slider('x')
st.write(x, 'squared is', x*x)