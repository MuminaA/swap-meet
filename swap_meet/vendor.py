

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
    # remove method
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
    # Swapping items method
    def swap_items(self, other_vendor, my_item, their_item):
        # if vendors inventory doesn't contain 'my_item' or friends inventory dosent contain 'their_item then return False
        # also if list empty return false
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            # remove my_item from my inventory
            index = self.inventory.index(my_item)
            removed_item = self.inventory.pop(index)
            # add my_item to friends inventory
            other_vendor.inventory.append(my_item)
            # remove their_item from friends inventory
            index = other_vendor.inventory.index(their_item)
            removed_item = other_vendor.inventory.pop(index)
            # add their_item to my inventory
            self.inventory.append(their_item)
            return True



# WAVE 4
    def swap_first_item(self, other_vendor):
        # if either inventory is empty, return false
        if not self.inventory or not other_vendor.inventory:
            return False
        
        # store the first item 
        my_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]

        # call the function from WAVE 3
        # 
        self.swap_items(other_vendor, my_first_item, other_first_item)
        return True


# WAVE 5
