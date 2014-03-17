# here is the weapon module
# a weapon has a type, damage and critical strike percent(chance)
# you do weapon + entity damage * 2 if you critical hit
from random import randint


class Weapon():
    # Weapon's constructor and to-string methods
    def __init__(self, type_, damage, critical_strike_percent):
        self.type = type_
        self.damage = damage

        if critical_strike_percent > 1.0 or critical_strike_percent < 0.0:
            critical_strike_percent = 0.0
        self.critical_strike_percent = critical_strike_percent

    def __str__(self):
        return "%s\n%d damage\n%d%% critical strike percent"\
            %(self.type, self.damage, self.critical_strike_percent * 100)


# returns True if weapon should do critical, else False
    def critical_hit(self):
        chance = randint(1, 100)
        
        if chance <= self.critical_strike_percent * 100:
            return True

        return False