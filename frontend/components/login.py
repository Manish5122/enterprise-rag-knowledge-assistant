import streamlit as st

from utils.api import login


def login_screen():

    st.title("🤖 Enterprise RAG")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        response = login(email, password)

        if "access_token" in response:

            st.session_state.logged_in = True

            st.session_state.token = response["access_token"]

            st.rerun()

        else:

            st.error(
                response.get(
                    "detail",
                    "Login Failed"
                )
            )

    st.write("")

    if st.button(
        "Create Account",
        use_container_width=True
    ):
        st.session_state.page = "signup"
        st.rerun()