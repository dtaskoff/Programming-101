def welcome():
    text = ["Welcome to the \"Do you even math?\" game!"
        "Here are your options:",
        "- start",
        "- highscore",
        "- exit"]

    print('\n'.join(text))

def welcome_player(player):
    print("Welcome {}! Let the game begin!".format(player))

def wrong_command():
    print("That's an incorrect command!")

def question(expression, number):
    print("Question #{}".format(number))
    print("What is the answer to {}?".format(expression))

def get_input():
    return input("?>")

def correct():
    print("Correct!")

def incorrect(score):
    print("Incorrect! Your score is {}".format(score))