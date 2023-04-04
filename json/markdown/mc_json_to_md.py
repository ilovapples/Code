import json


def get_json(jsonpath: str) -> dict:
  json_contents = open(jsonpath).read()
  
  json_contents_dict = json.loads(json_contents)
  return {"str": json_contents, "dict": json_contents_dict}


def json_to_md(json_path):
  json_contents = json.loads(open(json_path).read())
  
  if isinstance(json_contents, list):
    if "/" in json_path:
      md = '# ' + json_path[json_path.rindex("/")+1:json_path.rindex('.')] + '\n'
    else:
      md = '# ' + json_path[:json_path.rindex('.')] + '\n'
    
    for index, _dict in enumerate(json_contents):
      md += f'| Num: {index} |  |\n| - | - |\n'
      for key in _dict:
        md += f'| {key} | {json_contents[index][key]} |\n'
      md += '---\n'
  else:
    for key in json_contents:
      md += f'| {key} | {json_contents[key]} |\n'
  return md
print(json_to_md("Minecraft Items.json"))


order = ["id", "displayName", "name", "stackSize"]


def mc_json_to_md_horizontal(json_path):
  json_contents = json.loads(open(json_path).read())
  
  # if it's a list
  if isinstance(json_contents, list):
    if "/" in json_path:
      md = '# ' + json_path[json_path.rindex("/")+1:json_path.rindex('.')] + '\n| id | displayName | name | stackSize |\n| - | - | - | - |\n'
    else:
      md = '# ' + json_path[:json_path.rindex('.')] + '\n| id | displayName | name | stackSize |\n| - | - | - | - |\n'
    
    for index, _dict in enumerate(json_contents):
      for i in order:
        md += '| ' + str(_dict[i]) + ' '
      md += '|\n'
  
  # if it's not a list
  else:
    md += '---\n'
    for key in json_contents:
      md += f'| {key} | {json_contents[key]} |\n'
  return md
print(mc_json_to_md_horizontal("Minecraft Items.json"))
