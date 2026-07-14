from pathlib import Path
import streamlit as st

from utils.api import upload_pdf
from utils.session import logout


def sidebar():
    with st.sidebar:

        # ==========================
        # Logo
        # ==========================
        BASE_DIR = Path(__file__).resolve().parent.parent
        logo_path = BASE_DIR / "assets" / "logo.png"

        if logo_path.exists():
            st.image(str(logo_path), width=80)
        else:
            st.markdown("## 🤖 Enterprise RAG")

        st.caption("Knowledge Assistant")

        st.divider()

        # ==========================
        # New Chat
        # ==========================
        if st.button("➕ New Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        # ==========================
        # Upload PDF
        # ==========================
        st.subheader("📄 Upload Document")

        uploaded_file = st.file_uploader(
            "Choose a PDF",
            type=["pdf"],
            label_visibility="collapsed"
        )

        if uploaded_file is not None:

            with st.spinner("Uploading document..."):
                result = upload_pdf(uploaded_file)

            if "message" in result:
                st.success(result["message"])

                if "documents" not in st.session_state:
                    st.session_state.documents = []

                if uploaded_file.name not in st.session_state.documents:
                    st.session_state.documents.append(uploaded_file.name)

            else:
                st.error(result.get("detail", "Upload failed"))

        st.divider()

        # ==========================
        # Uploaded Documents
        # ==========================
        st.subheader("📚 Documents")

        if "documents" not in st.session_state:
            st.session_state.documents = []

        if st.session_state.documents:

            for doc in st.session_state.documents:
                st.write(f"📄 {doc}")

        else:
            st.caption("No documents uploaded")

        st.divider()

        # ==========================
        # Logout
        # ==========================
        if st.button("🚪 Logout", use_container_width=True):
            logout()