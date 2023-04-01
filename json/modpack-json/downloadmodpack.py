import requests
import os
import json

def dothething(file: str):
    thefile = open(file, 'r').read()
    thejson = json.loads(thefile)

    os.chdir('downloaded')
    folder = file[:file.find('.')]
    os.mkdir(folder)
    os.chdir(folder)

    for type in thejson['types']:
        os.mkdir(type)
        os.chdir(type)
        for project in thejson[type]:
            print(project)
            projectfile = requests.get(thejson[type][project]['directlink'], allow_redirects=True)
            extension = ''
            if type == 'mods':
                extension = '.jar'
            elif type == 'shaders' or type == 'datapacks':
                extension = '.zip'
            with open(thejson[type][project]['slug'] + extension, 'wb') as afile:
                afile.write(projectfile.content)
        os.chdir('..')

filename = 'terralith-computercraft.modpack.json'
dothething(filename)
print(f"Your files are in downloaded/{filename[:filename.find('.')]}/")