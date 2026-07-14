import streamlit as st


def login(token):

    st.session_state.logged_in = True
    st.session_state.token = token


def logout():

    st.session_state.logged_in = False
    st.session_state.token = None

    st.rerun()