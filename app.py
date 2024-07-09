import pdb
import pandas as pd
import streamlit as st
import user_actions.generate_email as generate_email
import user_actions.send_email as send_email
from util import *
import time

st.set_page_config(page_title="Instill AI SDR", 
                   layout="wide",)
st.title("Instill AI SDR")
title = st.title("Generate Emails")

if get_session("stage") is None:
    set_session("stage", "generate_email")

if get_session("sending_status"):
    pass

if get_session("emails") is None:
    set_session("emails", [])

if is_status("generate_email") or is_status("all_sent"):
    if is_status("all_sent"):
        title.title("All Emails Sent!")
    if is_status("generate_email"):
        title.title("Generate Emails")
    if get_session("auth_token") is None:
        auth_token = st.text_input('Auth Token:', type="password", value=st.secrets["INSTILL_CLOUD_API_TOKEN"])
        set_session("auth_token", auth_token)
    
    uploaded_file = st.file_uploader("Upload Your Client's Emails", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        set_session("stage", "uploaded_csv")
        for index, row in df.iterrows():
            email_row = {
                "receiver_email": row["client_email_address"],
                "sender_name": row["sender_name"],
                "email_subject": "",
                "email_content": "",
            }
            append_session("emails", email_row)

if is_status("uploaded_csv"):
    title.title("Upload Emails")
    if st.button('Generate Emails'):
        set_session("stage", "generating_emails")

if get_session("i") is None:
    set_session("i", 0)

if get_session("i") == len(get_session("emails")) and len(get_session("emails")) > 0:
    set_session("i", 0)
    set_session("emails", [])
    set_session("stage", "all_sent")
    st.rerun()

if is_status("generating_emails"):
    with st.spinner('Wait for it...'):
        email_rows = get_session("emails")
        i = get_session("i")
        with st.form(f"email_form_{i}"):
            if email_rows[i]["email_subject"] == "" or email_rows[i]["email_content"] == "":
                email_subject, email_content = generate_email.process(email_rows[i]["receiver_email"], email_rows[i]["sender_name"])
                time.sleep(0.3)
                email_rows[i]["email_subject"] = email_subject
                email_rows[i]["email_content"] = email_content
            email_rows[i]["email_subject"] = st.text_input("Email Subject", value=email_rows[i]["email_subject"])
            email_rows[i]["email_content"] = st.text_area("Email Content", value=email_rows[i]["email_content"], height=200)
            submit_button1 = st.form_submit_button(f"Send Email {i}")
        if submit_button1:
            send_email.process(email_rows[i]["email_subject"], email_rows[i]["email_content"], email_rows[i]["receiver_email"])
            submit_button1 = False

            st.write("Email sent!")
            i += 1
            set_session("i", i)
            st.rerun()

# TODO: Make it concurrently
email_rows = get_session("emails")
for j in range(len(email_rows)):
    if email_rows[j]["email_subject"] == "" or email_rows[j]["email_content"] == "":
        email_subject, email_content = generate_email.process(email_rows[j]["receiver_email"], email_rows[j]["sender_name"])
        email_rows[j]["email_subject"] = email_subject
        email_rows[j]["email_content"] = email_content