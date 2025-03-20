import streamlit as st

st.title('A Guide to Physics Revision 🐦‍⬛')

# audio_file = open("audio/YouTube_[YouAreTube.com].mp3", "rb")
# audio_bytes = audio_file.read()
#
# st.audio(audio_bytes, format="audio/mp3")

audio_file = open("audio/Spotify.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3")

clmn1, clmn2, clmn3 = st.columns(3)

with clmn1:
    st.page_link("pages/Vectors.py",
                 label="Vectors",
                 icon="📊",
                 use_container_width=True)

with clmn2:
    st.page_link("pages/Current_Electricity.py",
                 label="Current Electricity",
                 icon="🧙",
                 use_container_width=True)

with clmn3:
    st.page_link("pages/Waves.py",
                 label="Waves",
                 icon="🦗",
                 use_container_width=True)
