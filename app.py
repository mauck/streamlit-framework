import requests

# This is from the streamlit get started tutorial
# https://docs.streamlit.io/library/get-started/main-concepts

import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame(
	np.random.randn(10, 20),
	columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))