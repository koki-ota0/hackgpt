import os
import openai
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel
from typing import Annotated, List
import shutil
import json



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
  for line in lines:
    if line:
      speaker, message = line.split("：")
      if speaker != current_speaker:
        current_speaker = speaker
        conversations.append([(speaker, message)])
      else:
        conversations[-1].append((speaker, message))
  print(json.dumps(conversations))
  return json.dumps(conversations)


openai.api_key = os.environ['OPENAI_API_KEY']

prompt = f"""
グループディスカッションを始めてください。結論だけでなく、会話の過程を見せてください
登場人物は以下の三人：A(コンピュータに詳しい大学生)、B(体育会系の大学生でグループディスカッションは不慣れで喋りもあまりうまくない人)、 C(政治家を志す大学生で知識が豊富)
時間は全部で２分間で、そこまでに結論を出してください。
・テーマ：政治家に必要な能力とは何か？
・流れ：自己紹介→役割の決定→議論→結論まとめ
・役割：ファシリテーター(いろんな人に話を振り、議論の主導権を握る)、書記(みんなの発言や流れをドキュメントにまとめる)、タイムキーパー(議論が予定より後ろ倒しになっている時に残り時間を周りに伝える)
なお、３つの役割は、3人のうちの誰かがそれぞれ担当し、重複はないようにすること。担当は自己紹介後の約10秒間の間にに決めること
・A,B,C以外の話手は誰も登場させないでください。特に、ChatGPTはこの場に登場してはいけません。
では、始めて

"""
prompt = """
合コンのシミュレーションを始めてください。会話の過程を詳細に見せてください
・登場人物は、男女三人ずつの６人で、それらの性格はAIの生成に任せますが、できるだけいろんな性格やバックグラウンドや名前の人がいると良いでしょう。
・時間は実際には約2時間ですが、ここでは3~5分の会話とします。
・流れ：自己紹介→お互いの趣味や仕事の紹介→雑談
・参加者たちの目的は、将来的に付き合える異性を発見すること。最初は大人数での会話をしますが最終的には気の合う人と１対1での仲良い関係に持ち込みたいと思っている。そのため、途中でターゲットを絞ることが多い
・なので、共通の趣味になりそうなものがあったら積極的に食らいつく
・また合コンでは、異性の三人の性格を逐一詮索して、自分が付き合うとしたら誰が良いかを深く考えます。それと同時に、同性の他の二人よりも優位に立とうと、なるべく会話を引っ張ったり異性によく思われる発言をしがちです。
・基本的には、女性が男性に、男性が女性に、話を振る
・6人以外の話手は、ChatGPTも含めて誰も登場させないでください。
・途中で議論の出力が途絶えないように、一つの出力欄の中で、終わりまでの全ての会話を表示して
・3回に
"""
ans = get_completion_conversation(prompt)
print(ans)
