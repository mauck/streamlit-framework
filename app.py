import requests

# This is from the streamlit get started tutorial
# https://docs.streamlit.io/library/get-started/main-concepts

import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
	np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
	columns=['lat', 'lon'])

st.map(map_data)