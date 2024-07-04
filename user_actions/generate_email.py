from pipelines.process_pipelines import *
import json
import pdb
from util import *

def process(receiver_email, sender_name):
    
    urls = process_get_domain_urls(receiver_email)    
    
    company_urls = urls["company_urls"]
    product_urls = urls["product_urls"]
    person_urls = urls["person_urls"]

    company_info, product_info, person_info = ["123"], ["123"], ["123"]

    # TODO: make it concurrent
    # TODO: revert the json.loads if the output is list
    
    # for url in json.loads(company_urls):
    #     company_info.append(process_crawler(url["link"]))
    # for url in json.loads(product_urls):
    #     product_info.append(process_crawler(url["link"]))
    # for url in json.loads(person_urls):
    #     person_info.append(process_crawler(url["link"]))

    summary_response = process_summary(company_info, product_info, person_info)

    # TODO: check if the response is JSON
    summary_response = json.loads(summary_response)

    set_session("company_summary", summary_response["company"])
    set_session("person_summary", summary_response["person"])
    set_session("product_summary", summary_response["product"])
    
    generated_email = process_craft_cold_email_pipeline(summary_response, sender_name)

    return generated_email["subject"], generated_email["body"]