import requests

# This is from the streamlit get started tutorial
# https://docs.streamlit.io/library/get-started/main-concepts

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

df = pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
	})

df