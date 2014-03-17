# the dungeon module
import map_
import python, anaconda
import fight
import weapon, potion
from random import randint


# some data that is related only to the
# gameplay. it can be later changed and completed
# without breaking the whole thing

# python's health and damage get
# changed through the levels
# just like it should be
_python_base_health = 100
_python_health_per_level = 50
_python_base_damage = 0
_python_damage_per_level = 10

# anaconda's health and damage get
# changed through the levels too
_anaconda_base_health = 370
_anaconda_health_per_level = 40
_anaconda_base_damage = 10
_anaconda_damage_per_level = 20
_anaconda_base_berserk_chance = 4
_anaconda_berserk_critical =  1.50

# our humble set of weapons ^^ (for now)
_weapons_types = ["dagger", "staff", "bow", "rapier",
                    "elder rod", "snaken bow", "long sword"]

_weapons = {"dagger": (10, 0.0),
            "staff": (30, 0.25),
            "bow": (20, 0.80),
            "rapier": (25, 0.50),
            "elder rod": (30, 0.50),
            "snaken bow": (30, 1.00),
            "long sword": (35, 0.75)}


class Dungeon():
    # dungeon's constructor method
    def __init__(self, level, hero, max_level):
        self.map_ = map_.Map_("./maps/%s_map"%level)
        self.hero = hero
        self.level = int(level)
        self.max_level = int(max_level)

    # this spawns our hero at the top left corner of the map
    def spawn(self):
        self.position = (0, 0)
        self.map_.spawn()

    # returns the visible, to our hero, map
    def show_map(self):
        return self.map_.show_map(self.position)

    # gets the new coordinates as tuple depending
    # on 'direction' and current position
    def _get_new_position(self, direction):
        if direction == 'up':
            return self.position[0] - 1, self.position[1]
        elif direction == 'down':
            return self.position[0] + 1, self.position[1]
        elif direction == 'left':
            return self.position[0], self.position[1] - 1
        elif direction == 'right':
            return self.position[0], self.position[1] + 1
        else:
            return self.position

    # moves the hero through the map
    # return false is move isn't possible
    # i.e. the field is an obstacle or is outside the map
    def move(self, direction):
        new_position = self._get_new_position(direction)

        if not self.map_.on_map(new_position) or\
                self.map_.is_obstacle(new_position):
            return False

        if self.map_.is_gate(new_position):
            if not self.level_up():
                exit(0)
            return True
        elif self.map_.is_python(new_position):
            self.fight_with_python()
        elif self.map_.is_anaconda(new_position):
            self.fight_with_anaconda()
        elif self.map_.is_item(new_position):
            self.get_item()

        self.map_.update_map(self.position, new_position)
        self.position = new_position

        return True

    # returns us a sweet little python based on level
    def _get_python_for_current_level(self):
        return python.Python(_python_base_health + _python_health_per_level * self.level,
            _python_base_damage + _python_damage_per_level * self.level)

    # returns us a not so sweet giant anaconda,
    # that will probably eat us for breakfast
    def _get_anaconda_for_current_level(self):
        anaconda_berserk_tuple =\
            (_anaconda_base_berserk_chance + 1 - self.level,_anaconda_berserk_critical)
        return anaconda.Anaconda(_anaconda_base_health + _anaconda_health_per_level * self.level,
            _anaconda_base_damage + _anaconda_damage_per_level * self.level,
            anaconda_berserk_tuple)

    # here we fight with our little python
    def fight_with_python(self):
        python_ = self._get_python_for_current_level()
        fight_ = fight.Fight(self.hero, python_)
        fight_.simulate_fight()

    # here hero fights with an anaconda
    def fight_with_anaconda(self):
        anaconda_ = self._get_anaconda_for_current_level()
        fight_ = fight.Fight(self.hero, anaconda_)
        fight_.simulate_fight()

    # gets the map for the new level, spawns the hero
    # returns true and prints some messaged
    # if no more levels, returns false
    def level_up(self):
        if self.level >= self.max_level:
            print("you won!")
            return False

        self.level += 1
        print("nice, you got through this level")
        print("now it's time for the next one!")
        print("here be pythons..")
        print("-" * 40)
        self.map_ = map_.Map_("./maps/%s_map"%self.level)
        self.hero.take_healing(potion.Potion(self.hero.max_health))
        self.spawn()

        return True

    # get's our hero a weapon or a potion
    # based on (not so) completely random circumstances
    def get_item(self):
        chance = randint(1, 100)

        if chance >= 50:
            weapon_ = self.get_weapon()
            print("you found a %s"%weapon_)
            answer = input("do you want to pick it?(y, n)")
            if answer == 'y':
                self.hero.equip_weapon(weapon_)
                print("you got a new weapon!")
        else:
            potion_ = self.get_potion()
            self.hero.take_healing(potion_)
            print("you drank a potion!")

    # returns a random weapon from the set of weapons based on level
    # for level 1 - only the first one,
    # for level 2 - the first four ones and
    # for level 3 all weapons are available
    # (level 0 is a demo/test mode)
    def get_weapon(self):
        if self.level == 0:
            chance = randint(1, len(_weapons_types))
        else:
            chance = randint(1, (self.level * 3 - 3) or 1)

        type_ = _weapons_types[chance - 1]
        weapon_ = weapon.Weapon(type_,
            _weapons[type_][0],
            _weapons[type_][1])
        return weapon_

    # returns a potion healing 50% of our hero's missing health
    def get_potion(self):
        missing_health = self.hero.max_health - self.hero.health
        potion_ = potion.Potion(missing_health * 0.50)
        return potion_