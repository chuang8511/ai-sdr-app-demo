from pipelines.process_pipelines import *

def process(sending_email_subject, sending_email_content, receiver_email):
    print("Sending email to: ", receiver_email)
    print("Subject: ", sending_email_subject)
    print("Content: ", sending_email_content)
    pass
    # pdb.set_trace()    
    # process_send_email(sending_email_subject, sending_email_content, receiver_email)
    # return result