import logging
import sys
from typing import Dict, Tuple

import requests

from llama2 import Llama2Toolkit, parse_function_calling, parse_response

logging.basicConfig(level=logging.INFO)

URL = 'http://localhost:11434/api/generate'


def query_llama2(prompt: str) -> str:
    data = {'model': 'example', 'prompt': prompt}
    response = requests.post(URL, json=data).text
    return response


def query_mistral(prompt: str) -> str:
    data = {'model': 'mistral', 'prompt': prompt}
    response = requests.post(URL, json=data).text
    return response


def step_query(url: str) -> Tuple[str, Dict[str, str]]:
    toolkit = Llama2Toolkit(
        func=requests.get,
        description='Get content(html) from the URL',
        args=[
            {
                'name': 'url',
                'type': 'string',
                'description': 'The URL to get content from',
            }
        ]
    )
    prompt = toolkit.get_prompt(f'Summarize the content of the URL: {url}')
    response = query_llama2(prompt)
    parsed = parse_function_calling(response)
    return parsed


def step_visit(function_call: Tuple[str, Dict[str, str]]):
    func, args = function_call
    result = getattr(requests, func)(**args)
    return result.text


def step_summarize(content: str):
    prompt = f"""
    Summarize the content of HTML document.

    Devide content into three parts.
    - first: Summary of the content
    - second: The user comments with the most engagement. max 5 comments. user's name, comment, and the number of likes.
    - last: Summary of the comments.

    IMPORTANT: Respond in Korean.
    IMPORTANT: Do not include HTML tags in the response. Only the text content.

    below is the content:
    {content}
    """
    response = query_mistral(prompt)
    parsed = parse_response(response)
    return parsed


# Get function calling information
url = sys.argv[1]
query_result = step_query(url)
logging.info(f'URL: {url}')
logging.info(f'Generated function calling: {query_result}')

# Run function using the generated information
visit_result = step_visit(query_result)
logging.info(f'Visited content: {visit_result[:100]}...')

# Summarize the content
summary_result = step_summarize(visit_result)
print('=' * 50)
print(summary_result)
