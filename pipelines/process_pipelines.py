from .call_apis import call_api
from user_actions.util import chunk_info

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
    
def process_crawler(url):
    print("Processing crawler")
    data = {
        "inputs": [
            {
                "url": url
            }
        ]
    }


    response = call_api("crawler", data)["outputs"][0]
    return_val = []
    for result in response["webage_results"]:
        return_val.append(chunk_info(result["link-text"]))
    
    # ["link-text1", "link-text2", "link-text3]
    print("End crawler")
    return return_val


def process_summary(receiver_email, company_search_context, company_web_urls, person_search_context, person_web_urls, product_search_context, product_web_urls):
    data = {
        "inputs": [
            {
                "company_email": receiver_email,
                "company_search_context": company_search_context,
                "company_web_urls": company_web_urls,
                "person_search_context": person_search_context,
                "person_web_urls": person_web_urls,
                "product_search_context": product_search_context,
                "product_web_urls": product_web_urls
            }
        ]
    }

    response = call_api("summary", data)["outputs"][0]
    
    # JSON
    # {
    #   "company_summary": "summary",
    #   "product_summary": "summary",
    #   "person_summary": "summary",
    # }
    return response

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