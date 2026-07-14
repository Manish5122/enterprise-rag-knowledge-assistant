import streamlit as st

from utils.api import register


def signup_screen():

    st.title("Create Account")

    username = st.text_input("Username")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Register",
        use_container_width=True
    ):

        response = register(
            username,
            email,
            password
        )

        if "message" in response:

            st.success(response["message"])

            st.session_state.page = "login"

            st.rerun()

        else:

            st.error(
                response.get(
                    "detail",
                    "Registration Failed"
                )
            )

    st.write("")

    if st.button(
        "Back",
        use_container_width=True
    ):

        st.session_state.page = "login"

        st.rerun()