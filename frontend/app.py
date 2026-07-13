import streamlit as st
import requests

st.set_page_config(
    page_title="Enterprise RAG Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise RAG Knowledge Assistant")

try:
    response = requests.get("http://127.0.0.1:8000")
    response.raise_for_status()
    data = response.json()

    st.success("Backend Connected Successfully")
    st.json(data)

except Exception as e:
    st.error("Backend is not running")
    st.code(str(e))