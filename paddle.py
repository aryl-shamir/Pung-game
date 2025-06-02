from turtle import Turtle

# Distance the paddle moves on each keypress
MOVE_DISTANCE = 20

class Paddle(Turtle):
    """
    A class representing the paddle in the Pong game.

    Inherits from Turtle and handles vertical movement and initial setup.
    """

    def __init__(self, position):
        """
        Initialize a paddle at the given (x, y) position.

        Args:
            position (tuple): A tuple (x, y) specifying the initial location of the paddle.
        """
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)  # 5 units tall, 1 unit wide
        self.penup()
        self.goto(position)

    def go_up(self):
        """Move the paddle up by MOVE_DISTANCE units."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move the paddle down by MOVE_DISTANCE units."""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
