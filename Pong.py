# Pong Game in Python 3

import turtle # Module voor basic graphics
import winsound


# ***** WINDOW SETUP *****
window = turtle.Screen()
window.title("Pong by Maarten Warson")
window.bgcolor("maroon")
window.setup(width=800, height=600)
window.tracer(0) # Window updatet niet vanzelf => spel gaat sneller


# ***** FUNCTIONS *****
def create_paddle_a():
    paddle_a = turtle.Turtle() # Turtle-object
    paddle_a.speed(0) # Snelheid voor animatie (0 = maximum snelheid)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Width met 5 stretchen (standaard is het 20px op 20px)
    paddle_a.penup() # Er wordt géén lijn getekend waar paddle_a geweest is
    paddle_a.goto(-350, 0) # Startplaats
    return paddle_a

def create_paddle_b():
    paddle_b = turtle.Turtle() 
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)
    return paddle_b

def create_ball():
    ball = turtle.Turtle() 
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.4 # Iedere keer dat de bal beweegt over de X-as, beweegt het 0.2 pixel (naar rechts omdat het positief is) + geeft snelheid van beweging aan
    ball.dy = 0.4
    return ball

def create_pen():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle() # De pen verbergen (we willen alleen de tekst zien)
    pen.goto(0, 260)
    return pen

def paddle_a_up():
    if paddle_a.ycor() < 250: # Paddle kan niet buiten scherm gaan
        y = paddle_a.ycor() # y-coördinaat opvragen
        y += 20 # y-coördinaat gaat 20px omhoog
        paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() > -250:
        y = paddle_a.ycor() 
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() < 250:
        y = paddle_b.ycor() 
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > -250:
        y = paddle_b.ycor() 
        y -= 20
        paddle_b.sety(y)

def move_ball():
    # Over x-as
    x = ball.xcor()
    x += ball.dx
    ball.setx(x)
    # Over y-as
    y = ball.ycor()
    y += ball.dy
    ball.sety(y)

def update_score():
    pen.goto(0, 260)
    pen.write("Player A: {}   ||   Player B: {}".format(score_a, score_b), align="center", font=("Calibri", 18, "normal"))

def define_winner(winner):
    pen.goto(0, 50)
    pen.write("Player {} wins!".format(winner), align="center", font=("Calibri", 18, "normal"))
    pen.goto(0, 20)
    pen.write("Press <SPACEBAR> to play again", align="center", font=("Calibri", 14, "normal"))

def reset_game():
    global score_a # Verwijzen naar de globale variabele
    score_a = 0
    global score_b
    score_b = 0
    pen.clear()
    update_score()
    global game_ended
    game_ended = False


# ***** VARIABLES *****
score_a = 0
score_b = 0
end_score = 5
paddle_a = create_paddle_a()
paddle_b = create_paddle_b()
ball = create_ball()
pen = create_pen()
game_ended = True


# ***** Starttekst *****
pen.write("Player A: 0   ||   Player B: 0", align="center", font=("Calibri", 18, "normal"))
pen.goto(0, 20)
pen.write("Press <SPACEBAR> to start the game", align="center", font=("Calibri", 14, "normal"))


# KEYBOARD BINDING
window.listen() # Luistert naar keyboard input

window.onkeypress(paddle_a_up, "z") # Wanneer de 'z' wordt ingeduwd, wordt de paddle_a_up-functie aangesproken
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# ***** MAIN GAME LOOP => updatet window voortdurend waardoor de bal blijft bewegen*****
while True:
    window.update()

    if game_ended == False:
        move_ball()

    if game_ended == True:
        window.onkeypress(reset_game, "space")

    if score_a >= end_score or score_b >= end_score:
        game_ended = True
        
    if score_a == end_score:
        define_winner("A")

    if score_b == end_score:
        define_winner("B")

    # Bal tegen bovenrand
    if ball.ycor() > 290: # Hoogte van het venster is 600 => -300 en 300
        ball.sety(290)
        ball.dy *= -1 # Draait de richting om
        winsound.Beep(500, 100)

    # Bal tegen onderrand
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.Beep(500, 100)

    # Bal tegen rechterrand
    if ball.xcor() > 390:
        ball.goto(0, 0) # Ga naar het centrum
        ball.dx *= -1
        score_a += 1
        pen.clear() # Scoretekst leegmaken
        update_score()

    # Bal tegen linkerrand
    if ball.xcor() < -390:
        ball.goto(0 ,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        update_score()

    # Bal tegen rechter paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.Beep(200, 100)

    # Bal tegen linker paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.Beep(200, 100)