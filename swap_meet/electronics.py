from swap_meet.item import Item

class Electronics(Item):
    # WAVE 5
    def __init__(self, id=None, type='Unknown', condition=0):
        super().__init__(id, condition)

        self.type = type

    def __str__(self):
        return f"{super().__str__()} This is a {self.type} device."

    def get_category(self):
        return 'Electronics'

# ipad = (Electronics(12345, 'Ipad'))
# print(ipad.condition_description())
