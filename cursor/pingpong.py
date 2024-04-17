import time
import turtle

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
PADDLE_A_START_X = -250
PADDLE_B_START_X = 250
PADDLE_START_Y = 0
PADDLE_MOVE_DISTANCE = 20
BALL_START_DX = 5.0
BALL_START_DY = -5.0
SCORE_DISPLAY_X = 0
SCORE_DISPLAY_Y = 260
FONT = ("Courier", 24, "normal")
BALL_BORDER_TOP = 290
BALL_BORDER_BOTTOM = -290
BALL_BORDER_RIGHT = 390
BALL_BORDER_LEFT = -390
PADDLE_COLLISION_DISTANCE = 50
PADDLE_EDGE_RIGHT = 240
PADDLE_EDGE_LEFT = -240
SPEED_INCREMENT_FACTOR = 1.3

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
        self.window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        self.paddle_a = self.create_paddle(PADDLE_A_START_X, PADDLE_START_Y)
        self.paddle_b = self.create_paddle(PADDLE_B_START_X, PADDLE_START_Y)
        self.ball = self.create_ball()
        self.score_a = 0
        self.score_b = 0
        self.score_display = self.create_score_display()

        self.window.listen()
        self.window.onkeypress(self.paddle_a_up, "w")
        self.window.onkeypress(self.paddle_a_down, "s")
        self.window.onkeypress(self.paddle_b_up, "Up")
        self.window.onkeypress(self.paddle_b_down, "Down")

        self.last_move_time_a_front = time.time()  # Initialize last move time for paddle A
        self.last_move_time_b_front = time.time()  # Initialize last move time for paddle B
        
        # The rest of the __init__ method remains unchanged
        self.window.onkeypress(self.paddle_a_move_front, "d")  # Bind 'd' key for Player A to move front (right)
        self.window.onkeypress(self.paddle_b_move_front, "Left")  # Bind 'Left arrow' key for Player B to move front (left)



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
        ball.dx = BALL_START_DX
        ball.dy = BALL_START_DY
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
        score_display.goto(SCORE_DISPLAY_X, SCORE_DISPLAY_Y)
        score_display.write("Player A: 0  Player B: 0", align="center", font=FONT)
        return score_display

    def paddle_a_up(self):
        """
        Moves paddle A up.
        """
        y = self.paddle_a.ycor()
        y += PADDLE_MOVE_DISTANCE
        self.paddle_a.sety(y)

    def paddle_a_down(self):
        """
        Moves paddle A down.
        """
        y = self.paddle_a.ycor()
        y -= PADDLE_MOVE_DISTANCE
        self.paddle_a.sety(y)

    def paddle_b_up(self):
        """
        Moves paddle B up.
        """
        y = self.paddle_b.ycor()
        y += PADDLE_MOVE_DISTANCE
        self.paddle_b.sety(y)

    def paddle_b_down(self):
        """
        Moves paddle B down.
        """
        y = self.paddle_b.ycor()
        y -= PADDLE_MOVE_DISTANCE
        self.paddle_b.sety(y)

    def paddle_a_move_front(self):
        """
        Moves paddle A to the right (front for Player A) if 5 seconds have passed since the last front move.
        """
        if time.time() - self.last_move_time_a_front >= 5:  # Check if 5 seconds have passed
            x = self.paddle_a.xcor()
            x += PADDLE_MOVE_DISTANCE  # Move to the right
            if x < PADDLE_EDGE_RIGHT:  # Ensure paddle doesn't go beyond the game area
                self.paddle_a.setx(x)
            self.last_move_time_a_front = time.time()  # Update the last move time
            self.window.ontimer(self.reset_paddle_positions, 1000)  # Reset positions after 1 second


    def paddle_b_move_front(self):
        """
        Moves paddle B to the left (front for Player B) if 5 seconds have passed since the last front move.
        """
        if time.time() - self.last_move_time_b_front >= 5:  # Check if 5 seconds have passed
            x = self.paddle_b.xcor()
            x -= PADDLE_MOVE_DISTANCE  # Move to the left
            if x > -PADDLE_EDGE_RIGHT:  # Ensure paddle doesn't go beyond the game area
                self.paddle_b.setx(x)
            self.last_move_time_b_front = time.time()  # Update the last move time
            self.window.ontimer(self.reset_paddle_positions, 1000)  # Reset positions after 1 second

    def reset_paddle_positions(self):
        """
        Resets the paddle positions to their starting points.
        """
        self.paddle_a.goto(PADDLE_A_START_X, PADDLE_START_Y)
        self.paddle_b.goto(PADDLE_B_START_X, PADDLE_START_Y)

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
            if self.ball.ycor() > BALL_BORDER_TOP:
                self.ball.sety(BALL_BORDER_TOP)
                self.ball.dy *= -1

            if self.ball.ycor() < BALL_BORDER_BOTTOM:
                self.ball.sety(BALL_BORDER_BOTTOM)
                self.ball.dy *= -1

            if self.ball.xcor() > BALL_BORDER_RIGHT:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_a += 1
                self.update_score()

            if self.ball.xcor() < BALL_BORDER_LEFT:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_b += 1
                self.update_score()

            # Paddle collision
            if (self.ball.xcor() > PADDLE_EDGE_RIGHT - 10 and self.ball.xcor() < PADDLE_EDGE_RIGHT) and (self.ball.ycor() < self.paddle_b.ycor() + PADDLE_COLLISION_DISTANCE and self.ball.ycor() > self.paddle_b.ycor() - PADDLE_COLLISION_DISTANCE):
                self.ball.setx(PADDLE_EDGE_RIGHT)
                self.ball.dx *= -1

            if (self.ball.xcor() < PADDLE_EDGE_LEFT + 10 and self.ball.xcor() > PADDLE_EDGE_LEFT) and (self.ball.ycor() < self.paddle_a.ycor() + PADDLE_COLLISION_DISTANCE and self.ball.ycor() > self.paddle_a.ycor() - PADDLE_COLLISION_DISTANCE):
                self.ball.setx(PADDLE_EDGE_LEFT)
                self.ball.dx *= -1

    def update_score(self):
        """
        Updates the score display after a player scores.
        """
        self.score_display.clear()
        self.score_display.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align="center", font=FONT)

        # Increase ball speed by a certain percentage
        self.ball.dx *= SPEED_INCREMENT_FACTOR
        self.ball.dy *= SPEED_INCREMENT_FACTOR

if __name__ == "__main__":
    game = PingPongGame()
    turtle.mainloop()
