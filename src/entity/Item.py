import json

class Item:
    def __init__(self, item_id, name, title):
        self.item_id = item_id
        self.name = name
        self.title = title

        print(f'Item init | id: {self.item_id} | name : {self.name} | title : {self.title}')

    def __str__(self):
        return f'Item init | id: {self.item_id} | name : {self.name} | title : {self.title}'

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
