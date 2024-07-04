import json
from .call_apis import call_api

# ✅ TODO: Replace the data mapping
def process_get_domain_urls(receiver_email):
    data = {
        "inputs": [
            {
                "client-email": receiver_email
            }
        ]
    }
    
    response = call_api("get-domain-urls", data)["outputs"][0]
    
    # JSON
    # {
    #   "company_urls": [{"link": "https://"}],
    #   "person_urls": [{"link": "https://"}],
    #   "product_urls": [{"link": "https://"}],
    # }
    return response
    
    

# TODO: Replace the data mapping
def process_crawler(url):
    
    data = {
        "inputs": [
            {
                "url": url
            }
        ]
    }

    response = call_api("crawler", data)["outputs"][0]
    
    # String
    return response["web_info"]


# TODO: Replace the data mapping
def process_summary(company_info, product_info, person_info):
    data = {
        "inputs": [
            {
                "company_info": company_info,
                "person_info": product_info,
                "product_info": person_info
            }
        ]
    }

    response = call_api("summary", data)["outputs"][0]
    
    # JSON
    # {
    #   "company": "summary",
    #   "person": "summary",
    #   "product": "summary",
    #   "guideline": "summary"
    # }
    return response["summary"]

# TODO: Replace the data mapping
def process_craft_cold_email_pipeline(summary_response, sender_name):
    data = {
        "inputs": [
            {
                "company_summary": summary_response["company"],
                "person_summary": summary_response["person"],
                "product_summary": summary_response["product"],
                "sender_name": sender_name,
                "guideline": summary_response["guideline"]
            }   
        ]
    }

    response = call_api("craft-cold-email-pipeline", data)["outputs"][0]
    
    # JSON
    # { "body": "email body" 
    #   "subject": "email subject"
    # }
    return response

def process_send_email(sending_email_subject, sending_email_content, receiver_email):
    data = {
        "inputs": [
            {
                "subject": sending_email_subject,
                "body": sending_email_content,
                "receiver_email": receiver_email
            }
        ]
    }
    
    response = call_api("send-email", data)["outputs"][0]
    
    # String
    return response["sending_result"]