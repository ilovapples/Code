import json

def doit(file):
  thejson = open(file).read()

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
          if mod[key][i] != None:
            print(f"  {keys[i]}: {mod[key][i]}")
      else:
        print(f"{keys[key]}: {mod[key]}")
    print()

    
# example usage for the 'betterend.dependencies.json' file (an example dependencies file for the BetterEnd mod by quiqueck)
doit('betterend.dependencies.json')
