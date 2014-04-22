import ui
from expression_generator import ExpressionGenerator
from scoreboard import Scoreboard


class MathGame():
    def __init__(self):
        ui.welcome()
        self.question = 0
        self.player = "unknown"
        self.generator = ExpressionGenerator()
        self.scoreboard = Scoreboard()

    def loop(self):
        while True:
            commands = ui.get_input()
            self._parse(commands)

    def correct_guess(self):
        guess = ui.get_input()
        result = self.generator.get_value()

        if int(guess) == int(result):
            ui.correct()
            self.question += 1
            return True
        else:
            score = (self.question - 1) ** 2
            ui.incorrect(score)
            self.scoreboard.update(self.player, score)
            return False

    def play(self):
        self.generator.generate_new()
        expression = str(self.generator)
        ui.question(expression, self.question)

        return self.correct_guess()

    def start(self):
        self.question = 1
        self.player = ui.get_input()
        ui.welcome_player(self.player)
        while self.play(): pass

    def highscore(self):
        self.scoreboard.display()

    def exit(self):
        print("bye!")
        exit(0)

    def _parse(self, commands):
        try:
            getattr(self, commands)()
        except (TypeError, AttributeError):
            ui.wrong_command()