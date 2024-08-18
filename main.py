import turtle
import random
score = 0
FONT = ("Arial",30,"normal")


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

#score turtle
score_turtle = turtle.Turtle()

#coutdown turtle
coutdown_turtle = turtle.Turtle()
game_over = False
#turtle_list
turtle_list = []

# x y coordinatess
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_score_turtle():

    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()

    top_height = screen.window_height()/2
    y_height = top_height * 0.9
    score_turtle.goto(0,y_height)
    score_turtle.write(f"SCORE:{score}",False,"center",FONT)

grid_size = 10
def make_turtle(x,y):
    # instract turtle
    t = turtle.Turtle()
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"SCORE:{score}",False,"center",FONT)
        print(x,y)
    t.penup()
    t.shape("turtle")
    t.color("green")
    t.shapesize(2,2)
    t.goto(x * grid_size,y * grid_size)
    t.onclick(handle_click)
    t.pendown()
    turtle_list.append(t)


def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def turtle_hide():
    for t in turtle_list:
        t.hideturtle()
def show_turtle_random():
    if not game_over:
        turtle_hide()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_random,1000)

        #screen.ontimer(turtle_hide,1000)

def countdown_turtle(time):
    coutdown_turtle.color("dark blue")
    coutdown_turtle.hideturtle()
    coutdown_turtle.penup()
    global game_over
    top_height = screen.window_height() / 2
    y_height = top_height * 0.9
    coutdown_turtle.goto(0, y_height-30)
    coutdown_turtle.clear()

    if time > 0:
        coutdown_turtle.clear()
        coutdown_turtle.write(f"COUTDOWN    {time}", False, "center", FONT)
        screen.ontimer(lambda :countdown_turtle(time-1),1000)
    else:

        game_over = True
        coutdown_turtle.clear()
        coutdown_turtle.goto(0, 0)
        turtle_hide()

        coutdown_turtle.write(f"GAME OVER", False, "center", FONT)

def game_start_up():
    turtle.tracer(0)
    setup_turtle()
    setup_score_turtle()
    turtle_hide()
    show_turtle_random()
    countdown_turtle(10)
    turtle.tracer(1)


game_start_up()
turtle.mainloop()