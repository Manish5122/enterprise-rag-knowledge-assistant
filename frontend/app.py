import streamlit as st

from components.login import login_screen
from components.signup import signup_screen
from components.chat_ui import chat_screen


def load_css():
    with open("assets/styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="🤖",
    layout="wide",
)

if "page" not in st.session_state:
    st.session_state.page = "login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    chat_screen()

elif st.session_state.page == "login":
    login_screen()

else:
    signup_screen()