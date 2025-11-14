# pages/TrackQuery.py
import streamlit as st
import pandas as pd

st.title("🔎 Track Your Queries")
st.write("Status of current queries:")

# Example data for demonstration
data = {'Query ID': [1, 2], 'Status': ['In Progress', 'Completed']}
df = pd.DataFrame(data)

st.dataframe(df)
