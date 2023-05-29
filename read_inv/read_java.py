import sys
import python_nbt.nbt as nbt
import json

with open('en_us-item_key.json') as file:
    key = json.loads(file.read())


def get_from_item_key(id_index: str, key: dict={}):
    index = 'item.' + id_index.replace(':', '.')
    if not index in key.keys():
        index = 'block.' + id_index.replace(':', '.')
    return key[index]
    

def arg_exists(arg_num: int) -> bool:
    try:
        str(sys.argv[arg_num])
        return True
    except:
        return False
    

def read_item(item_nbt: dict):
    print(f"Item: \'{get_from_item_key(item_nbt['id'].value, key)}\' x{item_nbt['Count'].value}")
    extra = False
    if 'tag' in item_nbt.keys():
        extra = True
        if 'Damage' in item_nbt['tag'].keys():
            print(f"  Damage: {item_nbt['tag']['Damage'].value} pts")
            
        if 'display' in item_nbt['tag'].keys():
            if 'Name' in item_nbt['tag']['display']:
                print(f"  Custom Name: \'{json.loads(item_nbt['tag']['display']['Name'].value)['text']}\'")
            
            if 'Lore' in item_nbt['tag']['display']:
                print("  Lore: ")
                for line in item_nbt['tag']['display']['Lore'].value:
                    print(f"    {line.value}")
    if extra:
        print()    
            

def read_file(world_name: str, write_to_file: bool, single_player: bool) -> dict:
    print(f"Printing player items for world: '{world_name}' (in no specific order)\n")   
    data = nbt.read_from_nbt_file(world_name + '/level.dat')
    if single_player:
        for item in data['Data']['Player']['Inventory']:
            read_item(item)

def usage():
    print(f"usage: {sys.argv[0]} world_name [--single-player]")
    quit()


if __name__ == "__main__":
    write_json_to_file = False
    if '--write-json-to-file' in sys.argv:
        write_json_to_file = True
    if '--single-player' in sys.argv:
        single_player = True
    
    if not arg_exists(1):
        usage()
    read_file(sys.argv[1], write_json_to_file, single_player)