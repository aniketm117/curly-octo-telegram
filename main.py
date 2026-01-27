import streamlit as st

# Page title
st.set_page_config(page_title='What is Physics ?', page_icon='📚')
st.title('🛑 You are trespassing a private area')

# audio_file = open("audio/Spotify.mp3", "rb")
# audio_bytes = audio_file.read()
#
# st.audio(audio_bytes, format="audio/mp3")

st.image('img/stop_arnold.jpg',
         '67')

clmn1, clmn2, clmn3 = st.columns(3)

with clmn1:
    st.page_link("pages/Vectors.py",
                 label="Vectors",
                 icon="🏹",
                 use_container_width=True)

with clmn2:
    st.page_link("pages/Current_Electricity.py",
                 label="Current Electricity",
                 icon="🔋",
                 use_container_width=True)

with clmn3:
    st.page_link("pages/Waves.py",
                 label="Waves",
                 icon="🌊",
                 use_container_width=True)

clmn4, clmn5 ,clmn6 = st.columns(3)

with clmn4:
    st.page_link("pages/Fluid_Mechanics.py",
                 label="Fluid Mechanics",
                 icon="💧",
                 use_container_width=True)

with clmn5:
    st.page_link("pages/Kinematics.py",
                 label="Kinematics",
                 icon="🏀",
                 use_container_width=True)

with clmn6:
    st.page_link("pages/Roadmap.py",
                 label="Roadmap",
                 icon='🌉',
                 use_container_width=True)
