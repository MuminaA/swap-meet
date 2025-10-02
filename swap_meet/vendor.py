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
        self.swap_items(other_vendor, my_first_item, other_first_item)
        return True
    

# WAVE 6
# this is being override from item to clothing or decor or eletronic
# go through items of Vendor
# check if the category matached the category we are looking for

    def get_by_category(self, category):
        list_of_objects = []
        for item in self.inventory:
            if item.get_category() == category:
                list_of_objects.append(item)
        return list_of_objects

# get the best condition item in the list
    def get_best_by_category(self, category):
        best_item = None
        # start with a condition lower than 0
        best_condition = -1
        # loop through items of vendor
        for item in self.inventory:
            # if the category matched, then we compare conditions
            if item.get_category() == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        return best_item



    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # access vendor's list to get the best item in the category
        # which is the item the other vendor wants
        # used the get_best_by_category function
        they_want_the_best_item_in_my_inventory = self.get_best_by_category(their_priority)
        # access the other vendor's list to get the best item in the category
        # which is the item the vendor wants
        i_want_th_best_item_in_their_inventory =  other_vendor.get_best_by_category(my_priority)

        # no items matched, swap did not happen 
        if they_want_the_best_item_in_my_inventory is None or i_want_th_best_item_in_their_inventory is None:
            return False
    
        # use wave 3, swap_items(self, other_vendor, my_item, their_item)
        self.swap_items(other_vendor, they_want_the_best_item_in_my_inventory, i_want_th_best_item_in_their_inventory)
        return True
    




