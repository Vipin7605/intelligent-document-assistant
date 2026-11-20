
import streamlit as st
from pdf_processor import extract_text_from_pdf

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄"
)

st.title("📄 Intelligent PDF Document Assistant")
st.write("Upload a PDF and explore its contents.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    pages = extract_text_from_pdf(uploaded_file)

    st.write(f"Total pages: {len(pages)}")

    for page in pages:
        with st.expander(f"Page {page['page']}"):
            st.write(page["text"] or "No readable text found.")
