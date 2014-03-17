# and our python module(huh..)
import entity


class Python(entity.Entity):
    # python's constructor and to_string method
    # pretty simple, uses only entity's fields and methods
    def __init__(self, health, damage):
        super().__init__(health, damage)

    def __str__(self):
        return "snake:\n" + super().__str__()