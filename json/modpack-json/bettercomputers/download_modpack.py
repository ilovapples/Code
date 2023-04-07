from os import chdir, mkdir, path
import json
import yaml
import requests
import time


def mean(data: list) -> float:
    return sum(data)/len(data)


def download(file: str, yamlornot: bool) -> dict:
    """
    downloads shaders, datapacks, resourcepacks, and modpacks from 
    .modpack.json files (format created by me)

    Args:
        file (str): the name of the .modpack.json file to read from for modpack data information 
    """
    overall_start = time.time()

    if not path.isdir('downloaded'):
        mkdir('downloaded')

    with open(file, 'r', encoding='UTF-8') as thefiletoread:
        if not path.isdir('downloaded'):
            mkdir('downloaded')
            
        thefile = thefiletoread.read()
    
    if not yamlornot:
        thedata = json.loads(thefile)
    else:
        thedata = yaml.safe_load(thefile)

    chdir('downloaded')
    folder = file[:file.find('.')]
    if not path.isdir(folder):
        mkdir(folder)
    chdir(folder)
    
    if 'icon' in thedata['types']:
        icontimestart = time.time()
        with open('icon.png', 'wb') as theiconfile:
            iconfile = requests.get(
                thedata['icon'],
                allow_redirects=True,
                timeout=10
            )

            theiconfile.write(iconfile.content)

        icontimeend = time.time()
        print("Finished Downloading icon in %.5f seconds.\n" % (icontimeend - icontimestart))

    times = []

    for projecttype in thedata['types']:
        if not path.isdir(projecttype):
            mkdir(projecttype)
        chdir(projecttype)

        for project in thedata[projecttype]:
            downloadtimestart = time.time()
            projectfile = requests.get(
                thedata[projecttype][project]['directlink'],
                allow_redirects=True,
                timeout=10
            )
            extension = ''
            if projecttype == 'mods':
                extension = '.jar'
            else:
                extension = '.zip'

            file_name = project + extension

            with open(file_name, 'wb') as afile:
                afile.write(projectfile.content)
                downloadtimeend = time.time()
                print(f"Downloaded:   {file_name}")
                print("In: %.5f seconds.\n" % (downloadtimeend - downloadtimestart))
            times.append(downloadtimeend - downloadtimestart)

        chdir('..')
    overall_end = time.time()
    return {
        "overall": overall_end - overall_start,
        "downloadtimes": times
    }

if __name__ == '__main__':
    MAIN_FILE_NAME = 'shaders.yaml'
    thedownload = download(MAIN_FILE_NAME, True)
    print(f"Your files are in downloaded/{MAIN_FILE_NAME[:MAIN_FILE_NAME.find('.')]}/\n")
    print("Overall, it took %.5f seconds to download everything." % thedownload['overall'])
    print("The average time it took for a mod/shader/resourcepack/datapack to download was %.5f seconds." % mean(thedownload['downloadtimes']))
    print(f"Downloaded {len(thedownload['downloadtimes'])} files.")