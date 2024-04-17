import turtle

class PingPongGame:
    """
    A class to represent a Ping Pong game using the turtle graphics library.
    
    Attributes:
        window (turtle.Screen): The game window.
        paddle_a (turtle.Turtle): The left paddle.
        paddle_b (turtle.Turtle): The right paddle.
        ball (turtle.Turtle): The ball used in the game.
        score_a (int): The score for player A.
        score_b (int): The score for player B.
        score_display (turtle.Turtle): The turtle object used to display the score.
    """
    
    def __init__(self):
        """
        Initializes the game, creating the window, paddles, ball, and score display.
        Sets up keyboard bindings and starts the game loop.
        """
        self.window = turtle.Screen()
        self.window.title("Ping Pong")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)

        self.paddle_a = self.create_paddle(-250, 0)
        self.paddle_b = self.create_paddle(250, 0)
        self.ball = self.create_ball()
        self.score_a = 0
        self.score_b = 0
        self.score_display = self.create_score_display()

        self.window.listen()
        self.window.onkeypress(self.paddle_a_up, "w")
        self.window.onkeypress(self.paddle_a_down, "s")
        self.window.onkeypress(self.paddle_b_up, "Up")
        self.window.onkeypress(self.paddle_b_down, "Down")

        self.game_loop()

    def create_paddle(self, x, y):
        """
        Creates a paddle at the specified location.
        
        Parameters:
            x (int): The x-coordinate of the paddle.
            y (int): The y-coordinate of the paddle.
            
        Returns:
            turtle.Turtle: The created paddle.
        """
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=6, stretch_len=1)
        paddle.penup()
        paddle.goto(x, y)
        return paddle

    def create_ball(self):
        """
        Creates the ball used in the game.
        
        Returns:
            turtle.Turtle: The created ball.
        """
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 5.0
        ball.dy = -5.0
        return ball

    def create_score_display(self):
        """
        Creates the score display.
        
        Returns:
            turtle.Turtle: The turtle object used for the score display.
        """
        score_display = turtle.Turtle()
        score_display.speed(0)
        score_display.color("white")
        score_display.penup()
        score_display.hideturtle()
        score_display.goto(0, 260)
        score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
        return score_display

    def paddle_a_up(self):
        """
        Moves paddle A up.
        """
        y = self.paddle_a.ycor()
        y += 20
        self.paddle_a.sety(y)

    def paddle_a_down(self):
        """
        Moves paddle A down.
        """
        y = self.paddle_a.ycor()
        y -= 20
        self.paddle_a.sety(y)

    def paddle_b_up(self):
        """
        Moves paddle B up.
        """
        y = self.paddle_b.ycor()
        y += 20
        self.paddle_b.sety(y)

    def paddle_b_down(self):
        """
        Moves paddle B down.
        """
        y = self.paddle_b.ycor()
        y -= 20
        self.paddle_b.sety(y)

    def game_loop(self):
        """
        The main game loop. Handles ball movement, collision detection, and score updating.
        """
        while True:
            self.window.update()

            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Border checking
            if self.ball.ycor() > 290:
                self.ball.sety(290)
                self.ball.dy *= -1

            if self.ball.ycor() < -290:
                self.ball.sety(-290)
                self.ball.dy *= -1

            if self.ball.xcor() > 390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_a += 1
                self.update_score()

            if self.ball.xcor() < -390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_b += 1
                self.update_score()

            # Paddle collision
            if (self.ball.xcor() > 240 and self.ball.xcor() < 250) and (self.ball.ycor() < self.paddle_b.ycor() + 50 and self.ball.ycor() > self.paddle_b.ycor() - 50):
                self.ball.setx(240)
                self.ball.dx *= -1

            if (self.ball.xcor() < -240 and self.ball.xcor() > -250) and (self.ball.ycor() < self.paddle_a.ycor() + 50 and self.ball.ycor() > self.paddle_a.ycor() - 50):
                self.ball.setx(-240)
                self.ball.dx *= -1

    def update_score(self):
        """
        Updates the score display after a player scores.
        """
        self.score_display.clear()
        self.score_display.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align="center", font=("Courier", 24, "normal"))

if __name__ == "__main__":
    game = PingPongGame()
    turtle.mainloop()
