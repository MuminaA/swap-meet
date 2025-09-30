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