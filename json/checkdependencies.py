import json
import requests
import download_modpack
import dependencies

with open('BetterComputers.modpack.json') as jsonfile:
    thejsonfile = jsonfile.read()
dependencies = [dependencies.generate(project, False) for project in json.loads()]