from swap_meet.item import Item

class Decor(Item):
    # WAVE 5
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, condition)

        self.width = width
        self.length = length

    def __str__(self):
        return (f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space.")

    def get_category(self):
        return 'Decor'

# decor = (Decor(12345, 5, 10, 4))
# print(decor.condition_description())