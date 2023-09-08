# THIS PROGRAM HAS LIMITED FUNCTIONALITY FOR COMPLICATED RAW JSON FORMATTING IN ITEM NAMES

import sys
import os
import json
import python_nbt.nbt as nbt

with open('en_us-item_key.json', 'r', encoding='UTF-8') as file:
    key = json.loads(file.read())


def get_from_item_key(id_index: str, item_key: dict) -> str:
    """Takes an id/index and returns 

    Args:
        id_index (str): the id/index to check the key for to get the item name
        item_key (dict): the key to check for id_index

    Returns:
        str: the item name
    """
    index = 'item.' + id_index.replace(':', '.')
    if not index in item_key.keys():
        index = 'block.' + id_index.replace(':', '.')
    try:
        return item_key[index]
    except KeyError or IndexError:
        return 'ITEM NAME NOT FOUND'


def arg_exists(arg_num: int) -> bool:
    """Checks if the command-line argument at the given index exists

    Args:
        arg_num (int): the command-line argument index to check

    Returns:
        bool: True if the argument exists, False if not
    """
    try:
        str(sys.argv[arg_num])
        return True
    except IndexError:
        return False


def read_item(item_nbt: dict) -> dict:
    """Reads an item based off of the base nbt

    Args:
        item_nbt (dict): the base nbt to read off of

    Returns:
        dict: readable json to return
    """
    item_data = {}
    print(f"Item: \'{get_from_item_key(item_nbt['id'].value, key)}\' x{item_nbt['Count'].value}")
    item_data['name'] = get_from_item_key(item_nbt['id'].value, key)
    item_data['id'] = item_nbt['id'].value
    item_data['count'] = item_nbt['Count'].value
    extra = False
    if 'tag' in item_nbt.keys():
        extra = True
        item_data['extra'] = {}
        if 'Damage' in item_nbt['tag'].keys():
            print(f"  Damage: {item_nbt['tag']['Damage'].value} pts")
            item_data['extra']['damage'] = item_nbt['tag']['Damage'].value
        if 'display' in item_nbt['tag'].keys():
            if 'Name' in item_nbt['tag']['display']:
                if type(json.loads(item_nbt['tag']['display']['Name'].value)) == type({}):
                    print(f"  Custom Name: \'{json.loads(item_nbt['tag']['display']['Name'].value)['text']}\'")
                elif type(json.loads(item_nbt['tag']['display']['Name'].value)) == type([]):
                    print(f"  Custom Name: \'{json.loads(item_nbt['tag']['display']['Name'].value)[0]['text']}\'")
                item_data['extra']['custom_name'] = \
                    json.loads(item_nbt['tag']['display']['Name'].value)

            if 'Lore' in item_nbt['tag']['display']:
                print("  Lore: ")
                item_data['extra']['lore'] = []
                for line in item_nbt['tag']['display']['Lore'].value:
                    print(f"    {line.value}")
                    item_data['extra']['lore'].append(line.value)
                    
    if extra:
        print()
    return item_data


def read_file(world_name: str, write_to_file: bool, is_single_player: bool) -> dict:
    """reads all items (for all players if not singleplayer world) in a world

    Args:
        world_name (str): the name of the world folder to check for items
        write_to_file (bool): whether or not to write the results to a json file
        is_single_player (bool): whether or not to check for multiple players

    Returns:
        dict: the json data for the world's items 
    """
    print(f"Printing player items for world: '{world_name}' (in no specific order)\n")
    final_data = {}

    if is_single_player: # singleplayer world
        data = nbt.read_from_nbt_file(world_name + '/level.dat')
        final_data['items'] = []
        for item in data['Data']['Player']['Inventory']:
            final_data['items'].append(read_item(item))
    else: # multiplayer/server vanilla server
        cwd = os.getcwd()
        if 'world' in os.listdir():
            os.chdir('world/playerdata')
            for player_file in [i for i in os.listdir() if i.endswith('.dat')]:
                player_data = nbt.read_from_nbt_file(player_file)
                print(f"Printing items for player with hex UUID: {player_file[:player_file.rindex('.')]}")
                final_data[player_file[:player_file.rindex('.')]] = []
                for item in player_data['Inventory']:
                    final_data[player_file[:player_file.rindex('.')]].append(read_item(item))
                    

        elif world_name in os.listdir():
            os.chdir(f'{world_name}/world/playerdata')
            for player_file in [i for i in os.listdir() if i.endswith('.dat')]:
                player_data = nbt.read_from_nbt_file(player_file)
                print(f"Printing items for player with hex UUID: {player_file[:player_file.rindex('.')]}")
                final_data[player_file[:player_file.rindex('.')]] = []
                for item in player_data['Inventory']:
                    final_data[player_file[:player_file.rindex('.')]].append(read_item(item))
        os.chdir(cwd)
        
    if write_to_file:
        with open(f'written_json/{world_name}-player_items.json', 'w', encoding='UTF-8') as file2write:
            file2write.write(json.dumps(final_data, indent=4))
    return final_data

def usage():
    """Shows usage statement
    """
    print(f"usage: {sys.argv[0]} <world_name> [--write-json-to-file] [--single-player]")
    quit()


if __name__ == "__main__":
    WRITE_JSON_TO_FILE = False
    SINGLE_PLAYER = False
    if '--write-json-to-file' in sys.argv:
        WRITE_JSON_TO_FILE = True
    if '--single-player' in sys.argv:
        SINGLE_PLAYER = True
    
    if not arg_exists(1):
        usage()
    world_name = sys.argv[1]
 

    read_file(world_name, WRITE_JSON_TO_FILE, SINGLE_PLAYER)
    
    # read_file(sys.argv[1], WRITE_JSON_TO_FILE, SINGLE_PLAYER)