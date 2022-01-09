import requests

# This is from the streamlit get started tutorial
# https://docs.streamlit.io/library/get-started/main-concepts

import streamlit as st
import pandas as pd

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)