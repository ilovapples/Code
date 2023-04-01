from os import chdir, mkdir
import requests
import json

def dothething(file: str):
    thefile = open(file, 'r').read()
    thejson = json.loads(thefile)

    chdir('downloaded')
    folder = file[:file.find('.')]
    mkdir(folder)
    chdir(folder)

    for projecttype in thejson['types']:
        mkdir(projecttype)
        chdir(projecttype)
        for project in thejson[projecttype]:
            print(project)
            projectfile = requests.get(
                thejson[projecttype][project]['directlink'], allow_redirects=True
            )
            extension = ''
            if projecttype == 'mods':
                extension = '.jar'
            elif projecttype == 'shaders' or projecttype == 'datapacks':
                extension = '.zip'
            with open(thejson[projecttype][project]['slug'] + extension, 'wb') as afile:
                afile.write(projectfile.content)
        chdir('..')

filename = 'terralith-computercraft.modpack.json'
dothething(filename)
print(f"Your files are in downloaded/{filename[:filename.find('.')]}/")
