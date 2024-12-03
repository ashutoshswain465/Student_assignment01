import streamlit as st
import pandas
from sent_mail import sent_mail

df = pandas.read_csv("topics.csv")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email address")
    select_box = st.selectbox("What topic do you want to discuss?", df["topic"])
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {select_box}
{raw_message}
"""
    button = st.form_submit_button()

    if button:
        sent_mail(message)
        st.info("Your email was sent successfully")
