from os import chdir, mkdir
import json
import requests

def download(file: str):
    """
    downloads shaders, datapacks, resourcepacks, and modpacks from 
    .modpack.json files (format created by me)

    Args:
        file (str): the name of the .modpack.json file to read from for modpack data information 
    """
    with open(file, 'r', encoding='UTF-8') as thefile:
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
                    thejson[projecttype][project]['directlink'],
                    allow_redirects=True,
                    timeout=10
                )
                extension = ''
                if projecttype == 'mods':
                    extension = '.jar'
                elif projecttype == 'shaders' or projecttype == 'datapacks':
                    extension = '.zip'
                with open(thejson[projecttype][project]['slug'] + extension, 'wb') as afile:
                    afile.write(projectfile.content)
            chdir('..')

FILE_NAME = 'terralith-computercraft.modpack.json'
download(FILE_NAME)
print(f"Your files are in downloaded/{FILE_NAME[:FILE_NAME.find('.')]}/")
