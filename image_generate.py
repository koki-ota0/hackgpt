# dalleを用いて画像生成を行う
# 作成者beneyotta

import requests
from requests.structures import CaseInsensitiveDict
import os

import json

QUERY_URL = "https://api.openai.com/v1/images/generations"


def generate_images(prompt):
  headers = CaseInsensitiveDict()
  headers["Content-Type"] = "application/json"
  api_key = os.environ['OPENAI_API_KEY']
  headers["Authorization"] = f"Bearer {api_key}"

  data = """
    {
        """
  data += f'"model": "image-alpha-001",'
  data += f'"prompt": "{prompt}",'
  data += """
        "num_images":1,
        "size":"512x512",
        "response_format":"url"
    }
    """

  resp = requests.post(QUERY_URL, headers=headers, data=data)

  if resp.status_code != 200:
    raise ValueError("Failed to generate image " + resp.text)

  response_text = json.loads(resp.text)
  return response_text['data'][0]['url']


# ここのプロンプトをいじれば好きに画像生成できる
# python3 image_generate.py
# prompt = """So, the topic for today is "Strategies to
# increase the number of tourists to the ski resort in Hakuba village. Let's start by brainstorming some ideas."""
# prompt = "a man with cute smile"

# image_url = generate_images(prompt)
# print(image_url)
