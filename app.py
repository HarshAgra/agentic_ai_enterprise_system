import sys
import os

sys.path.append(os.getcwd())

import streamlit as st
from workflows.main_workflow import route_query

st.set_page_config(page_title="Agentic AI System", layout="wide")

st.title("🚀 Agentic AI Enterprise System (Project Pragna)")
st.markdown("Ask business queries across Support, HR, Finance, Procurement")

# Input box
query = st.text_input("Enter your query:")

# Button
if st.button("Get Answer"):
    if query:
        with st.spinner("Processing..."):
            response = route_query(query)
        st.success("Response:")
        st.write(response)
    else:
        st.warning("Please enter a query.")
