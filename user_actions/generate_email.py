from pipelines.process_pipelines import *
import json
from util import *
from .util import *
import asyncio
import aiohttp
import random
import time

def process(receiver_email, sender_name):
    # mock process
    time.sleep(3)

    return f"fake subject {random.randint(1, 10)}", f"fake body {random.randint(1, 10)}" 
    urls = process_get_domain_urls(receiver_email)    
    
    company_urls = urls["company_urls"]
    product_urls = urls["product_urls"]
    person_urls = urls["person_urls"]

    company_info, product_info, person_info = asyncio.run(run_all_urls(company_urls, product_urls, person_urls))

    company_web_urls, person_web_urls, product_web_urls = [], [], []

    for url in company_urls:
        company_web_urls.append(arrange_url(url))
    for url in product_urls:
        product_web_urls.append(arrange_url(url))
    for url in person_urls:
        person_web_urls.append(arrange_url(url))

    summary_response = process_summary(receiver_email, company_info, company_web_urls, person_info, person_web_urls, product_info, product_web_urls)

    set_session("company_summary", summary_response["company_summary"])
    set_session("person_summary", summary_response["person_summary"])
    set_session("product_summary", summary_response["product_summary"])

    # generated_email = process_craft_cold_email_pipeline(summary_response, sender_name)
    # return generated_email["subject"], generated_email["body"]
        
async def run_all_urls(company_urls, product_urls, person_urls):
    company_task = run_process_crawler_concurrently(company_urls)
    product_task = run_process_crawler_concurrently(product_urls)
    person_task = run_process_crawler_concurrently(person_urls)
    
    company_info, product_info, person_info = await asyncio.gather(company_task, product_task, person_task)
    
    return company_info, product_info, person_info
    
async def run_process_crawler_concurrently(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(async_crawl(url["link"], session))
        return await asyncio.gather(*tasks)
    
async def async_crawl(url, session):
    print("Processing crawler")
    data = {
        "inputs": [
            {
                "url": url
            }
        ]
    }
    url = "https://api.instill.tech/v1beta/users/leochen5/pipelines/sdr-crawler-pipeline/trigger"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_session("auth_token")}'
    }
    promise_response = await session.post(url, headers=headers, data=json.dumps(data))
    reader = await promise_response.content.read()
    
    response = json.loads(reader.decode("utf8"))['outputs'][0]
    return_val = []
    for result in response["webage_results"]:
        return_val.append(chunk_info(result["link-text"]))

    print("End crawler")
    return return_val