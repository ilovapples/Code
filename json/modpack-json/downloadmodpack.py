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
    with open(file, 'r', encoding='UTF-8') as thefiletoread:
        thefile = thefiletoread.read()
        thejson = json.loads(thefile)
        chdir('downloaded')
        folder = file[:file.find('.')]
        mkdir(folder)
        chdir(folder)

        for projecttype in thejson['types']:
            mkdir(projecttype)
            chdir(projecttype)
            for project in thejson[projecttype]:
                projectfile = requests.get(
                    thejson[projecttype][project]['directlink'],
                    allow_redirects=True,
                    timeout=10
                )
                extension = ''
                if projecttype == 'mods':
                    extension = '.jar'
                elif projecttype == 'shaderpacks' or projecttype == 'datapacks':
                    extension = '.zip'
                file_name = project + extension
                with open(file_name, 'wb') as afile:
                    afile.write(projectfile.content)
                print(f"Downloaded {file_name}")
            chdir('..')

JSON_FILE_NAME = 'BetterComputers.modpack.json'
download(JSON_FILE_NAME)
print(f"Your files are in downloaded/{JSON_FILE_NAME[:JSON_FILE_NAME.find('.')]}/")
