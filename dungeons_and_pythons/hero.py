# here's our hero module
# hero inherits entity

import entity

# that's again just in case
_base_attack_damage = 10


class Hero(entity.Entity):
    # class Hero's constructor and to-string methods
    def __init__(self, name, health, nickname, damage = _base_attack_damage):
        super().__init__(health, damage)
        self.max_health = health
        self.name = name
        self.nickname = nickname

    def __str__(self):
        return "%s:\n%s"%(self.known_as(), super().__str__())

    # returns a string with hero's name and nickname
    def known_as(self):
        return "%s the %s"%(self.name, self.nickname)

    # gets hero a new weapon
    # if she already had a weapon, it's lost
    def equip_weapon(self, weapon):
        self.weapon = weapon

    # returns True if hero is equipped with a weapon
    def has_weapon(self):
        return 'weapon' in self.__dict__

    # returns the damage that hero does,
    # i.e. true damage plus weapon damage,
    # which gets doubled if she crits
    def attack(self):
        damage = super().attack()

        if self.has_weapon():
            damage += self.weapon.damage
            if self.weapon.critical_hit():
                damage *= 2
        return damage

    # out hero drinks a health potion which gives her some
    # health points back.
    # health points can't go above max_health!
    def take_healing(self, healing_potion):
        if not self.is_alive():
            return False

        self.health += healing_potion.healing_points
        if self.health > self.max_health:
            self.health = self.max_health
        return True