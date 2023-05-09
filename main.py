import os
import openai
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel
import constants
import json
from image_generate import generate_images

openai.api_key = os.environ['OPENAI_API_KEY']


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=
    temperature,  # this is the degree of randomness of the model's output
  )
  return response.choices[0].message["content"]


def get_completion_conversation(prompt, model="gpt-3.5-turbo", temperature=0):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=
    temperature,  # this is the degree of randomness of the model's output
  )
  conversation = response.choices[0].message["content"].strip()
  # print(conversation)
  lines = conversation.split("\n")
  # print(lines)
  conversations = []
  current_speaker = None
  # for line in lines:
  #   if line:
  #     speaker, message = line.split("：")
  #     if speaker != current_speaker:
  #       current_speaker = speaker
  #       conversations.append([(speaker, message)])
  #     else:
  #       conversations[-1].append((speaker, message))
  # return json.dumps(conversations)
  return json.dumps(lines)


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


class Item(BaseModel):
  json_str: str


class Item2(BaseModel):
  command: str
  html: str


# 会話のためのクラス
class ItemSetting(BaseModel):
  scene: str
  theme: str
  person_names: list[str]
  person_personalities: list[str]


@app.get("/")
async def root():
  return {"message": "Hello World"}


# @app.post("/json2html")
# async def json2html(item: Item):
#   _json = item.json_str
#   prompt = "以下のJSONをHTMLに変換してください。:\n" + str(_json)
#   html = get_completion(prompt)
#   return html


@app.post("/setting")
async def setting(item: ItemSetting):
  print(item)
  prompt = ""
  if item.scene == "group-discussion":
    prompt = constants.GROUP_DISCUSSION_PROMPT(item)
  elif item.scene == "party":
    prompt = constants.JOINT_PART_PROMPT(item)
  elif item.scene == "first-meeting":
    prompt = constants.FIRST_MEETING_PROMPT(item)

  # ans = get_completion_conversation(prompt)
  ans = get_completion(prompt)
  # print(ans)
  return ans


# @app.get("/chat.html")
# async def read_chat_html():
#   with open("chat.html", "r") as f:
#     html = f.read()
#   return HTMLResponse(content=html, status_code=200)


# 画像生成用API by磯崎
@app.post("/AIpaint")
async def AIpaint(item: Item):
  print("ok")
  object = item.json_str
  image = generate_images(object)
  html = f"<img src={image}>"
  return html


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
