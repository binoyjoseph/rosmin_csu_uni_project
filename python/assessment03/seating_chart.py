import turtle

# 1 = Unavailable (red), 0 = Available (white)
# seats[row_index][col]: row_index 0 = Row 1 (bottom), 5 = Row 6 (top)
# Columns 0-5 = A-F (left section), 6-11 = G-L (right section)
seats = [
    [0, 1, 0, 1, 0, 1,   0, 0, 1, 0, 1, 0],  # Row 1
    [1, 0, 1, 0, 1, 1,   1, 1, 0, 1, 0, 0],  # Row 2
    [0, 0, 0, 1, 1, 1,   0, 1, 1, 0, 0, 1],  # Row 3
    [1, 0, 0, 0, 0, 1,   1, 0, 0, 1, 1, 0],  # Row 4
    [1, 1, 1, 0, 0, 0,   0, 0, 1, 0, 0, 1],  # Row 5
    [0, 1, 0, 0, 0, 0,   1, 0, 1, 1, 0, 1],  # Row 6
]

CELL = 60       # size of each seat cell
GAP = 20        # vertical gap between row pairs
LEFT_X = -400   # x start of left section (A-F)
RIGHT_X = 60    # x start of right section (G-L)
BASE_Y = -210   # y start of bottom row


def draw_square(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


screen = turtle.Screen()
screen.title("Python Turtle Graphics")
screen.bgcolor("lightgray")
screen.setup(1000, 700)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw seats
for row in range(6):
    y = BASE_Y + row * CELL + (row // 2) * GAP
    for col in range(12):
        x = LEFT_X + col * CELL if col < 6 else RIGHT_X + (col - 6) * CELL
        draw_square(t, x, y, CELL, "red" if seats[row][col] else "white")

# Row numbers between sections
for row in range(6):
    y = BASE_Y + row * CELL + (row // 2) * GAP + CELL // 3
    t.penup()
    t.goto(10, y)
    t.write(row + 1, align="center", font=("Arial", 14, "bold"))

# Column letters - left section
for i, letter in enumerate("ABCDEF"):
    t.penup()
    t.goto(LEFT_X + i * CELL + CELL // 2, BASE_Y - 38)
    t.write(letter, align="center", font=("Arial", 14, "bold"))

# Column letters - right section
for i, letter in enumerate("GHIJKL"):
    t.penup()
    t.goto(RIGHT_X + i * CELL + CELL // 2, BASE_Y - 38)
    t.write(letter, align="center", font=("Arial", 14, "bold"))

# Legend
draw_square(t, -360, BASE_Y - 100, 28, "white")
t.penup()
t.goto(-323, BASE_Y - 93)
t.write("Available", font=("Arial", 12, "normal"))

draw_square(t, -190, BASE_Y - 100, 28, "red")
t.penup()
t.goto(-153, BASE_Y - 93)
t.write("Unavailable", font=("Arial", 12, "normal"))

screen.update()
turtle.done()
