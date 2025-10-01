import uuid

class Clothing:
    # WAVE 5
    def __init__(self, id=None, fabric='Unknown', condition=0):
        if id is None:
            # create large unique numbers and make it an interger
            self.id = uuid.uuid4().int
        else:
            # if id already provided, the self.id will just use it
            self.id = id

        self.fabric = fabric
        self.condition = condition

    def __str__(self):
        return (f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric.")

    def get_category(self):
        return 'Clothing'

# print(Clothing(12345, 'floral'))