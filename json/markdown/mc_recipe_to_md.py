import json

def recipe_to_markdown(recipe: str, writetofile: bool=False, filename: str=None) -> str:
  data = json.loads(recipe)
  markdown = "| Col1 | Col2 | Col3 | Result |\n| - | - | - | - |\n| "
  for row in data['pattern']:
    for col in row:
      string = data['key'][col]['item'][
        data['key'][col]['item'].index(':')+1:
      ].replace('_', ' ').title()
      markdown += string + ' | '
      
    if row is data['pattern'][1]:
      markdown += data['result']['item'][
        data['result']['item'].index(':')+1:
      ].replace('_', ' ').title() + ' |'
    else:
      markdown += ' |'
      
    if not row is data['pattern'][2]:
      markdown += '\n| '
      
  if writetofile:
    with open(filename, 'w') as file:
      file.write(markdown)
      
  return markdown

if __name__ == '__main__':      
  
  with open('sponge_pistol_recipe.json', 'r') as file:
    recipe = file.read()
  
  print(recipe_to_markdown(recipe))