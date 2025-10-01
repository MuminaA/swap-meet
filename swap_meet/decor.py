class Decor:
    # WAVE 5
    def __init__(self, id=None, width=0, length=0, condition=0):
        if id is None:
            # create large unique numbers and make it an interger
            self.id = uuid.uuid4().int
        else:
            # if id already provided, the self.id will just use it
            self.id = id

        self.width = width
        self.length = length
        self.condition = condition

    def __str__(self):
        return (f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space.")

    def get_category(self):
        return 'Decor'

# print(Decor(12345, 5, 10))