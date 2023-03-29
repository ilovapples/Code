import requests
import json


def savetofile(data: str, filename: str) -> None:
    # Opens a file with the given filename in write mode and writes the given data to it
    with open(filename, 'w') as file:
        file.write(data)
        
        
def generate(modrinth_project: str) -> list:
    """
    This function generates a list of dictionaries containing information about the dependencies of the
    specified Modrinth project, and writes this data to a JSON file with a filename that corresponds to the 
    project name.

    Args:
        modrinth_project (str): name of the chosen project on Modrinth (as in: 'fabric-api' instead of 'Fabric API')

    Returns:
        list: the json data for the dependencies of the chosen Modrinth project.
    """
    # Get the JSON data for the project dependencies from the Modrinth API
    dependencies_jsontext = requests.get(f'https://api.modrinth.com/v2/project/{modrinth_project}/dependencies').text
    
    # Create an empty list to store the final output
    finaljson = []
    
    # Convert the JSON data to a Python object
    dependencies_json = json.loads(dependencies_jsontext)
    
    # Loop through the list of dependencies
    for mod in dependencies_json['projects']:
        # Create a dictionary of information about the dependency
        values = {
            "name": mod['title'],
            "slug": mod['slug'],
            "page": f'https://modrinth.com/{mod["project_type"]}/{mod["slug"]}',
            "external": {
                "wiki": mod['wiki_url'],
                "source": mod['source_url'],
                "issues": mod['issues_url']
            }
        }
        
        # Create a new dictionary with a subset of the information from the 'values' dictionary, and append it to the final output list
        finaljson.append(
            {
                "modname": values['name'], 
                "modslug": values['slug'],
                "modpage": values['page'],
                "external": {
                    "wiki": values['external']['wiki'],
                    "source": values['external']['source'],
                    "issues": values['external']['issues']
                }
            }
        )
        
    # Write the final output list to a JSON file with a filename corresponding to the project name
    savetofile(json.dumps(finaljson, indent=4), f'{modrinth_project}.dependencies.json')
    
    # Return the final output list
    return finaljson

    
if __name__ == '__main__':
    # Call the 'generate' function with the argument 'betterend', which will generate a JSON file with the name 'betterend.dependencies.json'
    generate('betterend')
