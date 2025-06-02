from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class to manage the scoreboard display for the Pong game.
    Inherits from Turtle.
    """

    def __init__(self, position):
        """
        Initialize the scoreboard at a specific screen position.

        Args:
            position (tuple): A tuple (x, y) representing the scoreboard's location.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(position)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Display the current score at the assigned position.
        """
        self.write(f"{self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        """
        Increment the score by one, clear the previous display,
        and update with the new score.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
