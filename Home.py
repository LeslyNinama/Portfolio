import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv', sep=';')

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.jpg", width=350)

with col2:
    st.title("Lesly Shreyash Ninama")
    content = """
    As a dedicated tech enthusiast with a fervent passion for innovation and problem-solving, I
bring a dynamic blend of technical expertise, creativity, and a relentless drive for excellence.
With a proven track record of embracing new technologies and staying abreast of industry
trends, I am committed to leveraging my skills and knowledge to contribute to cutting-edge
projects and drive impactful solutions. I am poised to make a significant impact in the
ever-evolving world of technology.
"""
    st.info(content)
st.text("Below You Can Find Some of the Apps I Have Built in Python. Feel free to contact me :)")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for i in range(0, len(data), 2):
        st.title(data['title'][i])
        st.image(f"images/{data['image'][i]}")
        st.info(data['description'][i])
        st.write(f"[Source Code]({data['url'][i]})")


with col4:
    for i in range(1, len(data), 2):
        st.title(data['title'][i])
        st.image(f"images/{data['image'][i]}")
        st.info(data['description'][i])
        st.write("[Source Code](https://pythonhow.com)")
