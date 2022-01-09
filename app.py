import requests

# This is from the streamlit get started tutorial
# https://docs.streamlit.io/library/get-started/main-concepts

import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
	}))