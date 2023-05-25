# Python Interpreter for PMCL (POG Mini Config Language)
"""POG Mini Config Language"""

def load(data: str) -> dict:
  final = {}
  
  for index, line in enumerate(data.split('\n')):
    separator = ''
    valtype = []
    if line.strip() == '':
      continue
    
    # all ':'s
    if ' : ' in line and not '=' in line:
      separator = ' : '
    elif ': ' in line and not '=' in line:
      separator = ': '
    elif ' :' in line and not '=' in line:
      separator = ' :'
    elif ':' in line and not '=' in line:
      separator = ':'
    # all '='s
    elif ' = ' in line and not ':' in line:
      separator = ' = '
    elif '= ' in line and not ':' in line:
      separator = '= '
    elif ' =' in line and not ':' in line:
      separator = ' ='
    elif '=' in line and not ':' in line:
      separator = '='
    else:
      return {"error": f"FormatError: On line {str(index+1)}, no valid key -> value separator was found."}
      
    if line[-1] == 'i':
      valtype = ['int', int, '']
    elif line[-1] == 'f':
      valtype = ['float', float, '']
    elif line[-1] == 's':
      valtype = ['str', str, 'yes']
    elif line[-1] == '"' and line.split(separator)[1][0] == '"':
      valtype = ['str', str, '']
    elif line[-1] == "'" and line.split(separator)[1][0] == "'":
      valtype = ['str', str, '']
    else:
      return {"error": f"FormatError: On line {str(index+1)}, the type is not defined."}
      
    try:
      if valtype[0] == 'str':
        if valtype[2] == 'yes':
          final[line.split(separator)[0]] = line.split(separator)[1][0:-1]
        else:
          final[line.split(separator)[0]] = line.split(separator)[1].replace('"','')
      else:
        final[line.split(separator)[0]] = valtype[1](line.split(separator)[1][0:-1])
    except:
      return {"error": f"FormatError: On line {str(index+1)}, the value '{line.split(separator)[1][0:-1]}' cannot be formatted to '{valtype[0]}'."}
  
  return final

if __name__ == '__main__':
  import json
  
  with open('test.pmcl') as file:
    print(json.dumps(load(file.read()), indent=4))
