# our gameplay module
import hero
import dungeon
import copy


# the current available heroes
# (you can get the full version for only $*****.. some other time)
_heroes = [ hero.Hero("sharik", 400, "pythonslayer", 40),
            hero.Hero("arya", 380, "shadow princess", 40),
            hero.Hero("silmarillion iv", 420, "lost king of pyland", 35)]

_heroes_by_name = { "sharik": _heroes[0],
                    "arya": _heroes[1],
                     "silmarillion": _heroes[2] }

class Gameplay():
    # gameplay's constructor
    def __init__(self, difficulty):
        self.difficulty = int(difficulty)

    # here we add the hero with name 'hero_name' to our game
    def add_hero(self, hero_name):
        hero_ = self.pick_a_hero(hero_name)
        starting_level = 1
        if self.difficulty == 0:
            starting_level = 0
        self.dungeon = dungeon.Dungeon(starting_level, hero_, self.difficulty)
        self.dungeon.spawn()

    # returns a hero object depending on 'hero_name'
    def pick_a_hero(self, hero_name):
        return copy.deepcopy(_heroes_by_name[hero_name])

    # returns all posible heroes to pick
    def list_heroes(self):
        heroes = ["\nheroes:"]
        for hero in _heroes_by_name:
            heroes.append("-" * 40)
            heroes.append(str(_heroes_by_name[hero]))
            heroes.append("-" * 40)
        return '\n'.join(heroes)

    # returns a string forming our hero's current vision
    # i.e. the fields that she can see from her own one
    def vision(self):
        return self.dungeon.show_map()

    # moves our hero in 'direction' and returns true if
    # the move is possible, else false
    def move(self, direction):
        return self.dungeon.move(direction)

    # returns our hero's status - health points and damage
    def status(self):
        return self.dungeon.hero

    # returns our hero's inventory
    # (for now, she can have only one weapon)
    def inventory(self):
        if 'weapon' not in self.dungeon.hero.__dict__:
            return "your inventory is empty"
        else:
            return self.dungeon.hero.weapon

    # prints some instructions to help playing the game
    def instructions(self):
        commands = "available commands:\n"\
                + "move <direction = up/down/right/left>\nstatus\ninventory\nexit"
        map_key = "\n\nmap key:\n"\
                + "A - anaconda\nP - python\nH - hero\nI - item\nG - gate"
        more_help = "\n\nreach the gate to go to the next level,\n"\
                + "but be careful with pythons and anacondas.\n"\
                + "they like to bite passing heroes!"

        return commands + map_key + more_help

    # returns true if we're still playing and
    # false if we've been eaten by a snake
    def in_game(self):
        return self.dungeon.hero.is_alive()