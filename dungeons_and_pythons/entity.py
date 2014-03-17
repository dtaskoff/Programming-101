# here's our entity module
# an entity has base health and damage
# you can't heal above that base health

# these here are just in case someone
# does something he doesn't understand
# (like me)
_base_health = 100
_base_attack_damage = 10


class Entity():
    # Entity's constructor and to-string methods
    def __init__(self, health = _base_health, damage = _base_attack_damage):
        self.damage = damage

        if health <= 0:
            health = _base_health

        self.health = health
        self.max_health = health

    def __str__(self):
        return "%d/%d health\n%d damage"\
            %(self.health, self.max_health, self.damage)

    # returns health points of entity
    def get_health(self):
        return self.health

    # reduces entity's health points by 'damage'.
    # health points is always a number equal or greater than 0!
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # returns True if entity is alive,
    # i.e. has health points greater than zero
    def is_alive(self):
        return self.health > 0

    # returns entity's true damage, i.e.
    # without weapons and stuff
    def attack(self):
        return self.damage