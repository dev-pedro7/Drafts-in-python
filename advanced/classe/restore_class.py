import json
path = "./"
path += "save_class.json"

with open('save_class.json', 'r') as archive:
    dog_breed = json.load(archive)
    print(dog_breed)