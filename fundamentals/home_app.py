import streamlit as st

from .app_template_app import main as template
from .buttons_app import main as buttons
from .components_app import main as components
from .container_app import main as container
from .layouts_app import main as layouts
from .media_files_app import main as media_files
from .progress_display_app import main as progress_display
from .select_widget_app import main as select_widget
from .sidebar_app import main as sidebar
from .table_display_app import main as table_display
from .text_display_app import main as text_display
from .text_inputs_app import main as text_input
from .theme_app import main as theme

PRFX = "fundamentals_home"


def main():
    menu = [
        "Home",
        "AppTemplate",
        "Buttons",
        "Components",
        "Container",
        "Layouts",
        "MediaFiles",
        "ProgressDisplay",
        "SelectWidget",
        "SideBar",
        "TableDiaplay",
        "TextDisplay",
        "TextInputs",
        "Theme",
    ]
    choice = st.sidebar.selectbox("SubMenu", menu, key=f"{PRFX}_submenu")

    if choice == "Home":
        st.subheader("Home")
        st.image("resources/fundamentals_info.png")
    elif choice == "AppTemplate":
        st.title(f"Fundamentals - {choice}")
        template()
    elif choice == "Buttons":
        st.title(f"Fundamentals - {choice}")
        buttons()
    elif choice == "Components":
        st.title(f"Fundamentals - {choice}")
        components()
    elif choice == "Container":
        st.title(f"Fundamentals - {choice}")
        container()
    elif choice == "Layouts":
        st.title(f"Fundamentals - {choice}")
        layouts()
    elif choice == "MediaFiles":
        st.title(f"Fundamentals - {choice}")
        media_files()
    elif choice == "ProgressDisplay":
        st.title(f"Fundamentals - {choice}")
        progress_display()
    elif choice == "SelectWidget":
        st.title(f"Fundamentals - {choice}")
        select_widget()
    elif choice == "SideBar":
        st.title(f"Fundamentals - {choice}")
        sidebar()
    elif choice == "TableDiaplay":
        st.title(f"Fundamentals - {choice}")
        table_display()
    elif choice == "TextDisplay":
        st.title(f"Fundamentals - {choice}")
        text_display()
    elif choice == "TextInputs":
        st.title(f"Fundamentals - {choice}")
        text_input()
    elif choice == "Theme":
        st.title(f"Fundamentals - {choice}")
        theme()
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
