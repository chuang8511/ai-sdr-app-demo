import tiktoken

def arrange_url(url):
    return f'# {url["title"]}\n* URL: {url["link"]}\n{url["snippet"]}'

def chunk_info(info):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = string_to_tokens(info, encoding)
    if len(tokens) <= 8000:
        return info
    else:
        middle_range = len(tokens) // 2
        reply_tokens = tokens[middle_range-4000:middle_range+4000]
        return tokens_to_string(reply_tokens, encoding)

def string_to_tokens(info, encoding):
    return encoding.encode(info)

def tokens_to_string(tokens, encoding):
    return encoding.decode(tokens)