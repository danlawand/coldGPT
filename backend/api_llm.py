import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY_HUGGING')
api_url = os.getenv('API_LLM_URL')

def llm_query(question, context):
    API_URL = api_url
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "inputs": {
            "question": question,
            "context": context
    },
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    return data['answer']
