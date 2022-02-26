from pathlib import Path
from pydoc import doc
import streamlit as st

# File Processing Pkgs
from PIL import Image
import pandas as pd
import docx2txt

from PyPDF2 import PdfFileReader
import pdfplumber

# Load Images
@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


def read_details(file):
    file_details = {
        "filename": file.name,
        "filetype": file.type,
        "filesize": file.size,
    }
    return file_details


def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()

    return all_page_text


def save_uploaded_file(file):
    tempdir = Path("tempDir")
    tempdir.mkdir(parents=True, exist_ok=True)
    with open(tempdir.joinpath(file.name), "wb") as f:
        f.write(file.getbuffer())

    return st.success(f"Saved file {file.name} in tempDir.")


def main():
    menu = ["Home", "Dataset", "DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            # To See details
            st.write(type(image_file))
            # Methods/Attributes
            # st.write(dir(image_file))
            st.write(read_details(image_file))
            # Load image
            st.image(load_image(image_file))
            # Save File
            save_uploaded_file(image_file)

    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if data_file is not None:
            # To See details
            st.write(type(data_file))
            st.write(read_details(data_file))
            # Load data
            df = pd.read_csv(data_file)
            st.dataframe(df)
            # Save File
            save_uploaded_file(data_file)

    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])
        # Save File
        if docx_file is not None:
            save_uploaded_file(docx_file)
        if st.button("Process"):
            if docx_file is not None:
                # To See details
                st.write(type(docx_file))
                st.write(read_details(docx_file))
                # Load documents
                if docx_file.type == "text/plain":
                    # Read as bytes
                    # raw_text = docx_file.read()  # works but in bytes
                    # st.write(raw_text)  # does work as excepted
                    # Read as string (decode bytes to string)
                    raw_text = str(docx_file.read(), encoding="utf-8")
                    # st.write(raw_text) # Works
                    st.text(raw_text)  # Works

                elif docx_file.type == "application/pdf":
                    # try:
                    #     with pdfplumber.open(docx_file) as pdf:
                    #         for page in pdf.pages:
                    #             st.write(page.extract_text())
                    # except:
                    #     st.write("None")

                    # using PyPDF
                    raw_text = read_pdf(docx_file)
                    st.write(raw_text)

                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)  # works
                    # st.text(raw_text) # works

    else:
        st.subheader("About")
        st.image("resources/fileupload_tuts_streamlit_jcharistech02.png")


if __name__ == "__main__":
    main()
