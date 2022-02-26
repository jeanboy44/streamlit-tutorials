import streamlit as st

from .file_download_app.app import main as file_download
from .file_upload_app.app import main as file_upload
from .tasklist_app.app import main as tasklist


PRFX = "applications_home"


def main():
    menu = ["Home", "FileDownloadApp", "FileUploadApp", "TaskListApp"]
    choice = st.sidebar.selectbox("SubMenu", menu, key=f"{PRFX}_cases")
    st.title(f"Applications - {choice}")
    if choice == "Home":
        st.subheader("Home")
    elif choice == "FileDownloadApp":
        st.sidebar.write("------------------")
        st.sidebar.markdown("# Application Menu")
        file_download()
    elif choice == "FileUploadApp":
        st.sidebar.write("------------------")
        st.sidebar.markdown("# Application Menu")
        file_upload()
    elif choice == "TaskListApp":
        st.sidebar.write("------------------")
        st.sidebar.markdown("# Application Menu")
        tasklist()
    else:
        pass


if __name__ == "__main__":
    main()
