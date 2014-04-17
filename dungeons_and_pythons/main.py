# the script that runs the whole game
import gameplay


# briefly: gets input from the keyboard to manipulate
# the whole action in a cycle that runs
# until we win or we get eaten
def main():
    print("welcome to dungeons and pythons v0.00!")
    print("-" * 40)
    difficulty = int(input("choose a difficulty(1-3): "))
    if difficulty > 3 or difficulty < 1:
        difficulty = 0
        print("you chose an invalid difficulty! demo mode started")
    game = gameplay.Gameplay(difficulty)
    print(game.list_heroes())

    hero_name = input("choose a hero: ")

    while hero_name not in gameplay._heroes_by_name:
        print("you entered incorrect name")
        hero_name = input("choose a hero: ")

    game.add_hero(hero_name)

    while game.in_game():
        print("\nmap:\n%s"%game.vision())
        command = input()
        command = command.split()
        if len(command) == 0:
            continue
        if command[0] == 'instructions':
            print(game.instructions())
        elif command[0] == 'status':
            print(game.status())
        elif command[0] == 'inventory':
            print(game.inventory())
        elif command[0] == 'move':
            if len(command) > 1:
                 if not game.move(command[1]):
                    print("you cannot go there..")
        elif command[0] == 'exit':
            exit(0)


if __name__ == '__main__':
    main()