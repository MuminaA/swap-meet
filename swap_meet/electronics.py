class Electronics:
    # WAVE 5
    def __init__(self, id, type='Unknown', condition=0):
        if id is None:
            # create large unique numbers and make it an interger
            self.id = uuid.uuid4().int
        else:
            # if id already provided, the self.id will just use it
            self.id = id

        self.type = type
        self.condition = condition

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def get_category(self):
        return 'Electroincs'

print(Electronics(12345, 'Ipad'))
