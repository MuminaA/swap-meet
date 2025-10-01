

class Vendor:
# WAVE 1
    def __init__(self, inventory=None):
        # if inventory is none then set an empty list by default
        if inventory is None:
            inventory = []
        # attribute (allows us to access inventory later)
        self.inventory = inventory
    # add method
    def add(self, item):
        # append the item to the inventory and return item
        self.inventory.append(item)
        return item

    def remove(self, item):
        # check if item is not in inventory rhen return False
        if item not in self.inventory:
            return False
        else:
            # remove the item from the inventory using pop method
            # (first get index of item) then return the removed item
            index = self.inventory.index(item)
            removed_item = self.inventory.pop(index)
            return removed_item

# WAVE 2
    def get_by_id(self, id):
        for item in self.inventory:
            # check if the item id match with a given id
            if item.id == id:
                return item
        # no matching item in the inventory
        return None

# WAVE 3
    def swap_items(self, other_vendor, my_item, their_item):
        # if vendors inventory doesn't contain 'my_item' or friends inventory dosent contain 'their_item then return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            print('item not avaliable')
            return False
        else:
            # print('both items exist')
            # removes `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
            # removes `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
            return True

