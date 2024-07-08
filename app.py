import streamlit as st
import user_actions.generate_email as generate_email
import user_actions.send_email as send_email
from util import set_session, get_session, is_status

st.title("Instill AI SDR ")
title = st.title("Click button to generate email")

if get_session("stage") is None:
    set_session("stage", "generate_email")

if get_session("sending_status"):
    title.title("Email Sent!")

if is_status("generate_email"):
    if get_session("auth_token") is None:
        auth_token = st.text_input('Auth Token:', type="password", value=st.secrets["INSTILL_CLOUD_API_TOKEN"])
        set_session("auth_token", auth_token)

    receiver_email = st.text_input('Your Client\'s Email:', value="chuang@netprotections.co.jp")
    sender_name = st.text_input('Your Name:', value="ChunHao")   
    
    if st.button('Generate Email'):
        email_subject, email_content = generate_email.process(receiver_email, sender_name)
        set_session("email_content", email_content)
        set_session("email_subject", email_subject)
        set_session("receiver_email", receiver_email)
        set_session("sender_name", sender_name)
        set_session("stage", "edit_email")
        st.rerun()
        

if is_status("edit_email"):
    title.title("Edit Email Below")
    st.header("Client's Company Summary")
    st.write(get_session("company_summary"))

    st.header("Client's Summary")
    st.write(get_session("person_summary"))

    st.header("Client's product Summary")
    st.write(get_session("product_summary"))

    sending_email_subject = st.text_input('Draft Email Subject:', value=st.session_state["email_subject"])
    sending_email_content = st.text_area('Draft Email:', value=st.session_state["email_content"], height=400)
    
    if st.button('Send Email'):
        send_email.process(sending_email_subject, sending_email_content, st.session_state["receiver_email"])
        set_session("sending_status", True)
        set_session("stage", "generate_email")
        st.rerun()
        