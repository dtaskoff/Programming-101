# our potion class
# the hardest one in the whole module, I think
class Potion():
    # our potion's constructor and to-string methods
    def __init__(self, healing_points):
        self.healing_points = healing_points

    def __str__(self):
        return "healing potion: %d hp"%self.healing_points