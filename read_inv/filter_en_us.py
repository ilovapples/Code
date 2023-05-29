FILE_KEY_NAME = 'en_us' # file name without '.json'

with open(FILE_KEY_NAME + '.json', 'r', encoding='UTF-8') as file:
    data = file.read()

final = "{\n"
for line in data.split('\n'):
    if "item.minecraft." in line or "block.minecraft." in line:
        final += line + '\n'
        print("Added to key: " + str(
            {line.strip()
            .replace('"',"")
            .replace(",","")
            .split(': ')[0]: line.strip()
                .replace('"',"")
                .replace(",","")
                .split(': ')[1]}
        ))
final += "\n}"
with open(f"{FILE_KEY_NAME}-item_key.json", 'w', encoding='UTF-8') as file:
    file.write(final[::-1].replace(',','',1)[::-1])
