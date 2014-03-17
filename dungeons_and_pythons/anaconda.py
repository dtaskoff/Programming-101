# the anaconda module
# anaconda inherits python (o.O)
import python


class Anaconda(python.Python):
    # anaconda's constructor and to-string methods
    def __init__(self, health, damage, berserk_tuple):
        super().__init__(health, damage)
        self.berserk_tuple = berserk_tuple
        self.attacks_till_berserk = self.berserk_tuple[0]

    def __str__(self):
        return "big %s\n%d/%d%% berserk"\
            %(super().__str__(), self.berserk_tuple[0], self.berserk_tuple[1] * 100)

    # returns the damage that anaconda deals,
    # i.e. true damage that gets multiplied if she's
    # berserk. the first member of 'berserk_tuple' is how
    # often will she go mad (e.g. every 4th or 3rd attack) and 
    # the second member is the berserk_factor, i.e.
    # by what number is the output damage multiplied
    def attack(self):
        damage = super().attack()
        self.attacks_till_berserk -= 1

        if self.attacks_till_berserk == 0:
            damage *= self.berserk_tuple[1]
            self.attacks_till_berserk = self.berserk_tuple[0]

        return damage