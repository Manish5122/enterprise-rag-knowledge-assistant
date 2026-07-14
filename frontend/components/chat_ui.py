import streamlit as st

from components.sidebar import sidebar
from utils.api import ask_question


def chat_screen():

    sidebar()

    st.title("🤖 Enterprise RAG Knowledge Assistant")
    st.caption("Powered by FastAPI • FAISS • Ollama")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous conversation
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message["role"] == "assistant" and "sources" in message:
                with st.expander("📚 Sources"):
                    st.write(f"Retrieved Chunks : {message['sources']}")

    # Chat Input
    prompt = st.chat_input(
        "Ask anything about your uploaded documents..."
    )

    if prompt:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # Assistant response
        with st.chat_message("assistant"):

            thinking = st.empty()
            thinking.markdown("⏳ Thinking...")

            try:

                result = ask_question(prompt)

                thinking.empty()

                answer = result.get(
                    "answer",
                    "No answer received."
                )

                st.markdown(answer)

                with st.expander("📚 Sources"):
                    st.write(f"Retrieved Chunks : {result.get('sources', 0)}")

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": result.get("sources", 0)
                    }
                )

            except Exception as e:

                thinking.empty()

                st.error(f"Backend Error: {e}")
                