import uuid

# WAVE 2
class Item:
    # default id to none to start
    def __init__(self, id=None, condition = 0):
        if id is None:
            # create large unique numbers and make it an interger
            self.id = uuid.uuid4().int
        else:
            # if id already provided, the self.id will just use it
            self.id = id
        
        self.condition = condition

    def get_category(self):
        # we want to see this override in WAVE 5*
        return "Item"

# WAVE 3
    def __str__(self):
        return (f"An object of type Item with id {self.id}.")
    
# WAVE 5 
    def condition_description(self):
        