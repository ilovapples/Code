import json

thejson = open("dependencies.json").read()

mods = json.loads(thejson)

keys = {
  'modname': 'Name', 
  'modslug': 'Slug', 
  'modlink': 'Jar Link', 
  'modpage': 'Website', 
  'external': 'External Sites', 
  'required': 'Required',
  'wiki': 'Wiki',
  'source': 'Source Code',
  'issues': 'Issues Page'
}


for mod in mods:
  for key in mod.keys():
    if key == 'external':
      print(f"{keys[key]}: ")
      for i in mod[key]:
        if mod[key][i] != '':
          print(f"  {keys[i]}: {mod[key][i]}")
    else:
      print(f"{keys[key]}: {mod[key]}")
  print()
