import sys
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
    except IndexError:
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
                print(f"  Custom Name: \' \
                      {json.loads(item_nbt['tag']['display']['Name'].value)['text']}\'")
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
    data = nbt.read_from_nbt_file(world_name + '/level.dat')
    final_data = {}

    if is_single_player:
        final_data['items'] = []
        for item in data['Data']['Player']['Inventory']:
            final_data['items'].append(read_item(item))
    if write_to_file:
        with open(f'{world_name}-player_items.json', 'w', encoding='UTF-8') as file2write:
            file2write.write(json.dumps(final_data, indent=4))
    return final_data

def usage():
    """Shows usage statement
    """
    print(f"usage: {sys.argv[0]} world_name [--write-json-to-file] [--single-player]")
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

    read_file(sys.argv[1], WRITE_JSON_TO_FILE, SINGLE_PLAYER)
