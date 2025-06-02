from turtle import Turtle


class Ball(Turtle):
    """
    A class to represent the ball in the Pong game.

    Inherits from Turtle and handles the movement, bouncing, and resetting of the ball.
    """

    def __init__(self):
        """Initialize the ball at the center with default movement and speed."""
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Move the ball in its current direction by updating x and y coordinates.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Invert the y-direction of the ball to simulate bouncing off a wall.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Invert the x-direction of the ball and increase its speed slightly
        to make the game more challenging.
        """
        self.x_move *= -1
        self.move_speed *= 0.9  # Speed up the ball after hitting a paddle

    def goto_center(self):
        """
        Reset the ball to the center of the screen and reverse its direction.
        This is typically called when a point is scored.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
