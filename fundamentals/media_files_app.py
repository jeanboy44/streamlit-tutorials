import streamlit as st
from PIL import Image


def main():
    col1, col2 = st.columns(2)

    with col1:
        st.title("Result")
        # # Display Images
        img = Image.open("resources/image_03.jpg")
        st.image(img, use_column_width=True)

        # # From URL
        st.image(
            "https://media.istockphoto.com/photos/innovation-and-science-concept-picture-id1177116437"
        )

        # Display Videos
        video_file = open("resources/secret_of_success.mp4", "rb").read()
        st.video(video_file, start_time=3)

        # Display Audio/Working with Audio
        audio_file = open("resources/song.mp3", "rb")
        st.audio(audio_file.read())
    with col2:
        code = """import streamlit as st
from PIL import Image

st.title("Result")
# # Display Images
img = Image.open("resources/image_03.jpg")
st.image(img, use_column_width=True)

# # From URL
st.image(
    "https://media.istockphoto.com/photos/innovation-and-science-concept-picture-id1177116437"
)

# Display Videos
video_file = open("resources/secret_of_success.mp4", "rb").read()
st.video(video_file, start_time=3)

# Display Audio/Working with Audio
audio_file = open("resources/song.mp3", "rb")
st.audio(audio_file.read())"""
        st.title("Code")
        st.code(code)


if __name__ == "__main__":
    main()
