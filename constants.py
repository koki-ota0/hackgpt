# promptを生成する関数まとめ
from main import ItemSetting


def GROUP_DISCUSSION_PROMPT(item):
  scene = item.scene
  theme = item.theme
  names = item.person_names
  personalities = item.person_personalities
  persons_prompt = ""
  for i in range(len(names)):
    persons_prompt += names[i] + "で性格は" + personalities[i] + '\n'
  persons_prompt += "です。"
  prompt = f"""
  {scene}を始めてください。結論だけでなく、会話の過程を見せてください
  では次に、以下のようなルールを付け足します。時間は全部で10分間で、そこまでに結論を出してください。
  ・テーマ：{theme}
  ・流れ：自己紹介→役割の決定→議論→結論まとめ
  ・役割：ファシリテーター(いろんな人に話を振り、議論の主導権を握る)、書記(みんなの発言や流れをドキュメントにまとめる)、タイムキーパー(議論が予定より後ろ倒しになっている時に残り時間を周りに伝える)
  人数が{len(names)}人でそれぞれメンバーは
  {persons_prompt}
  なお、３つの役割はメンバーのうちの誰かがそれぞれ担当し、重複はないようにすること。担当は自己紹介後の約10秒間の間にに決めること
  ・上記メンバー以外の話手は誰も登場させないでください。特に、ChatGPTはこの場に登場してはいけません。
  では、始めて

  """
  return prompt


def JOINT_PART_PROMPT(item: ItemSetting):
  member_num = len(item.person_names)
  prompt = f"""
  合コンのシミュレーションを始めてください。会話の過程を詳細に見せてください
・人数：男女{member_num}人ずつの{member_num*2}人

・性格やバックグランド：AIの生成に任せますが、できるだけいろんな性格やバックグラウンドや名前の人がいると良いでしょう。
・時間は実際には約2時間ですが、ここでは3~5分の会話とします。
・流れ：自己紹介→お互いの趣味や仕事の紹介→雑談
・6人以外の話手は、ChatGPTも含めて誰も登場させないでください。
・途中で議論の出力が途絶えないように、一つの出力欄の中で、終わりまでの全ての会話を表示して

合コンの会話の出力にあたって意識するべきこと
・参加者たちの目的は、将来的に付き合える異性を発見すること。最初は大人数での会話をしますが最終的には気の合う人と１対1での仲良い関係に持ち込みたいと思っている。そのため、途中でターゲットを絞ることが多い
・なので、共通の趣味になりそうなものがあったら積極的に食らいつく
・また合コンでは、異性の三人の性格を逐一詮索して、自分が付き合うとしたら誰が良いかを深く考えます。それと同時に、同性の他の二人よりも優位に立とうと、なるべく会話を引っ張ったり異性によく思われる発言をしがちです。
・基本的には、女性が男性に、男性が女性に、話を振る
  """
  return prompt


def FIRST_MEETING_PROMPT(item):
  member_num = len(item.person_names)
  personalities = item.person_personalities
  names = item.person_names
  persons_prompt = ""
  for i in range(len(names)):
    persons_prompt += names[i] + "で性格は" + personalities[i] + '\n'
  persons_prompt += "です。"
  prompt = f"""
  今から、以下の人間になりきって、以下の内容のような会話をしてください。なお、シチえーションとしては、初対面で打ち解けようとしている場面だとします。
・人数：{member_num}人
・参加者の情報
・{persons_prompt}
・詳細なシチュエーション：{item.theme}
  """
  return prompt


# 詳細なシチュエーション：２人は初対面で、大学でおんなじクラスに配属された。そのため、高原はこれから磯崎と打ち解けられたら良いと思っているが、磯崎はあまり多くを語りたがらず、当初、高原が話を振ってもあまり発言しなかったが、高原はそのコミュニケーションスキルにより磯崎の口数を増やそうと試みる。磯崎に、自らの人見知りを意識させないようなナチュラルな会話を試みる