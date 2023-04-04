import json
# import download_modpack
import dependencies

with open('BetterComputers.modpack.json', 'r', encoding='UTF-8') as jsonfile:
    thejsonfile = jsonfile.read()
    modpackjson = json.loads(thejsonfile)
    depslist = []
    for projtype in modpackjson['types']:
        for project in modpackjson[projtype].keys():
            depslist.append(dependencies.generate(project, False))
    print(modpackjson['mods'].keys())
    