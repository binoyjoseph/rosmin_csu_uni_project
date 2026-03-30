import turtle
import random

# Function to generate spots with availability and unavailability
# spots[row_index][col]: row_index 0 = Row 1 (bottom), 5 = Row 6 (top)
# Columns 0-5 = A-F (left section), 6-11 = G-L (right section)
def generate_spots(rows, cols, availability):
    spots = []
    for i in range (rows):
        # Empty row
        row = []
        for _ in range(cols):
            random_value = random.random()
            if random_value > availability:
                row.append('unavailable')
            else:
                row.append('available')
        # end inner loop
                
        # Add the row to the main list
        spots.append(row)
    # end outer loop
    
    return spots
# End function

# Function to draw a square
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
# End function

# Constants
ROWS = 6
COLS = 12
CELL = 60       # size of each spot cell
GAP = 20        # vertical gap between row pairs
LEFT_X = -400   # x start of left section (A-F)
RIGHT_X = 60    # x start of right section (G-L)
BASE_Y = -210   # y start of bottom row

print('Welcome to the Utopia Parking Availability Visualizer!')
print('Please enter the check-in time to see parking availability')
# TODO Add validations
check_in_hour = int(input(">> Enter check-in hour (0-23):  "))
print('Choose a background colour (lightgrey, skyblue, yellow)')
bg_colour = input(">> Background colour (default: lightgrey):") or "lightgrey"
print('Choose an unavailable spot colour (red, green, blue).')
unavail_spot_colour = input(">> Enter unavailable spot colour (Default: red):") or "red"

availability = 0
if (check_in_hour > 0 and check_in_hour <= 6) or (check_in_hour >= 18 and check_in_hour <=23):
    availability = 80
elif check_in_hour >= 7 and check_in_hour <= 11:
    availability = 20
elif check_in_hour >= 12 and check_in_hour <= 17:
    availability = 50
else:
    print("Enter a valid time: ")

print("Average parking availability: ", availability, "%")
print("Background color", bg_colour)
print("Spot color", unavail_spot_colour)
availability_percent = availability / 100


# Generate 2-d array of parking spots
spots = generate_spots(ROWS, COLS, availability_percent)
print(spots)

# Draw with turtle
screen = turtle.Screen()
screen.title("Python Turtle Graphics")
screen.bgcolor(bg_colour)
screen.setup(1000, 700)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw parking pots
for row in range(ROWS):
    y = BASE_Y + row * CELL + (row // 2) * GAP
    for col in range(COLS):
        x = LEFT_X + col * CELL if col < (COLS/2) else RIGHT_X + (col - (COLS/2)) * CELL
        draw_square(t, x, y, CELL, unavail_spot_colour if spots[row][col] == "unavailable"  else "white")

# Row numbers between sections
for row in range(ROWS):
    y = BASE_Y + row * CELL + (row // 2) * GAP + CELL // 3
    t.penup()
    t.goto(10, y)
    t.write(row + 1, align="center", font=("Arial", 14, "bold"))

# Column letters - left section
CODE_A = 65
for i in range(6):
    t.penup()
    t.goto(LEFT_X + i * CELL + CELL // 2, BASE_Y - 38)
    letter = chr(CODE_A + i)
    t.write(letter, align="center", font=("Arial", 14, "bold"))

# Column letters - right section
for i in range(6):
    t.penup()
    t.goto(RIGHT_X + i * CELL + CELL // 2, BASE_Y - 38)
    letter = chr(CODE_A + ROWS + i)
    t.write(letter, align="center", font=("Arial", 14, "bold"))

# Legend for Available
draw_square(t, -360, BASE_Y - 100, 28, "white")
t.penup()
t.goto(-323, BASE_Y - 93)
t.write("Available", font=("Arial", 12, "normal"))

# Legend for Unavailable
draw_square(t, -190, BASE_Y - 100, 28, unavail_spot_colour)
t.penup()
t.goto(-153, BASE_Y - 93)
t.write("Unavailable", font=("Arial", 12, "normal"))

screen.update()
turtle.done()