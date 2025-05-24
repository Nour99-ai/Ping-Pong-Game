
import turtle

# Set up the window for the game
window = turtle.Screen()
window.title("Ping Pong by Nour")         # Window title
window.bgcolor("black")                   # Background color
window.setup(width=800, height=600)       # Window size
window.tracer(0)                          # Turn off auto-updating (manual updates for smooth animation)

# Initialize score variables for both players
score1 = 0
score2 = 0

# Paddle 1 (Left side, purple)
paddle1 = turtle.Turtle()
paddle1.speed(0)                          # Animation speed (0 = fastest)
paddle1.shape("square")
paddle1.color("purple")
paddle1.shapesize(stretch_wid=5, stretch_len=1)  # Make paddle tall and thin
paddle1.penup()                           # Don't draw lines when moving
paddle1.goto(-350, 0)                     # Start position on the left

# Paddle 2 (Right side, cyan)
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("cyan")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)                      # Start position on the right

# Ball setup
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)                           # Start in the center
ball.dx = 4                               # Ball movement in x direction (speed)
ball.dy = 4                               # Ball movement in y direction (speed)

# Score display setup
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()                # Hide the turtle icon
score_display.goto(0, 260)                # Position at the top center

def update_score():
    """Update the score display at the top of the screen."""
    score_display.clear()
    score_display.write(f"{score1} : {score2}", align="center", font=("Courier", 24, "normal"))

update_score()  # Show initial score

# Paddle movement functions with boundary checks
def paddle1_up():
    """Move the left paddle up, unless at the top edge."""
    y = paddle1.ycor()
    if y < 250:
        y += 35
        paddle1.sety(y)

def paddle1_down():
    """Move the left paddle down, unless at the bottom edge."""
    y = paddle1.ycor()
    if y > -250:
        y -= 35
        paddle1.sety(y)

def paddle2_up():
    """Move the right paddle up, unless at the top edge."""
    y = paddle2.ycor()
    if y < 250:
        y += 35
        paddle2.sety(y)

def paddle2_down():
    """Move the right paddle down, unless at the bottom edge."""
    y = paddle2.ycor()
    if y > -250:
        y -= 35
        paddle2.sety(y)

# Keyboard bindings for paddle controls
window.listen()
window.onkeypress(paddle1_up, "w")        # W key moves left paddle up
window.onkeypress(paddle1_down, "s")      # S key moves left paddle down
window.onkeypress(paddle2_up, "Up")       # Up arrow moves right paddle up
window.onkeypress(paddle2_down, "Down")   # Down arrow moves right paddle down

def game_loop():
    """Main game loop: moves the ball, checks for collisions, updates score, and schedules next frame."""
    global score1, score2

    # Move the ball by its current speed
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off top and bottom borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse vertical direction
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball goes past right paddle: Player 1 scores
    if ball.xcor() > 390:
        score1 += 1
        update_score()
        ball.goto(0, 0)        # Reset ball to center
        ball.dx *= -1          # Send ball in opposite direction

    # Ball goes past left paddle: Player 2 scores
    if ball.xcor() < -390:
        score2 += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Ball collision with right paddle
    if (340 < ball.xcor() < 350) and (paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1          # Reverse horizontal direction

    # Ball collision with left paddle
    if (-350 < ball.xcor() < -340) and (paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    window.update()            # Refresh the screen
    window.ontimer(game_loop, 10)  # Schedule next frame in 10 ms

# Start the game loop
game_loop()

# Allow the user to close the window gracefully
window.mainloop()
