import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")

st.header("Contact Me")
with st.form(key="submit"):
    email = st.text_input("Email")
    subject = st.text_input("Subject")
    raw_message = st.text_area("Message")
    message = f"""\
Subject: {subject}

From: {email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info('Email Sent Successfully')
