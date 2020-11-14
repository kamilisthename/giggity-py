import src.entity.Item as Item
import src.exception.ItemNotFoundException
import json


class TempDB:
    def __init__(self):
        print('Temporary DB initiated')
        self.store = list()

    def save(self, item: Item):
        """
        :param item: Item to save in db
        :return: Item itself
        :rtype: Item
        """

        self.store.append(item)
        return Item

    def get_item_by_id(self, item_id: int):
        """
        :param item_id: Item ID to receive
        :return: Item/None
        :rtype: Item/None
        :exception: No item found
        """
        try:
            return [item for item in self.store if item.item_id == item_id][0]
        except src.exception.ItemNotFoundException as e:
            return None

    def remove(self, item_id: int):
        """
        :param item_id: Item ID to be removed
        :return: None
        """

        item = self.get_item_by_id(item_id)

        if item:
            self.store.remove(item)

    def find_all(self):
        """
        :return: List containing all items in store
        :rtype: list
        """

        return [item.to_json() for item in self.store]
