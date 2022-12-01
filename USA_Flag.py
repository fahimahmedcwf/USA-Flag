import turtle
import time
scr = turtle.getscreen()
scr.title("Flag of America")
scr.bgcolor("white")
t = turtle.Turtle()
t.speed(20)
t.penup()
flag_ht = 250
flag_wth = 475
x1 = -250
y1 = 120
stripe_ht = flag_ht/13
stripe_wdt = flag_wth
# star size
star_size = 12
def draw_rectangle(x, y, height, width, color):
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()
def star_shape(x, y, color, length):
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range(0, 5):
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()
def draw_stripes():
    x = x1
    y = y1
    for stripe in range(0, 6):
        for color in ["red", "white"]:
            draw_rectangle(x, y, stripe_ht, stripe_wdt, color)
            y = y - stripe_ht
    draw_rectangle(x, y, stripe_ht, stripe_wdt, 'red')
    y = y - stripe_ht
def draw_square():
    square_ht = (7/13) * flag_ht
    square_wdt = (0.76) * flag_ht
    draw_rectangle(x1, y1, square_ht, square_wdt, 'navy')
def stars1():
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 112
    for row in range(0, 5):
        x = -234
        for star in range(0, 6):
            star_shape(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines
def stars_five():
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 100
    for row in range(0, 4):
        x = -217
        for star in range(0, 5):
            star_shape(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines
time.sleep(5)
draw_stripes()
draw_square()
stars1()
stars_five()
t.hideturtle()
scr.mainlo
