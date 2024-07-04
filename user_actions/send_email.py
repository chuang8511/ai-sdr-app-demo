from pipelines import process_send_email

def process(sending_email_subject, sending_email_content, receiver_email):
    result = process_send_email(sending_email_subject, sending_email_content, receiver_email)
    return result