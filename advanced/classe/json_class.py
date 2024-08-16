import json
path = './'
path += 'save_class.json'

class Dog:
    def __init__(self, raca):
        self.raca = raca

dog = Dog('Damalta')

with open('save_class.json', 'w') as archive:
    json.dump(vars(dog), archive)
        