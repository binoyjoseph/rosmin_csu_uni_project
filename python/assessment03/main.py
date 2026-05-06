import turtle
import random

# Function to generate spots, two dimensional list with availability and unavailability. 
def generate_spots(rows, cols, availability):
    spots = []
    # Outer loop to create rows.
    for i in range (rows):
        # Empty row
        row = []
        # Inner loop to create columns within each row.
        for _ in range(cols):
            random_value = random.random()
            if random_value > availability:
                row.append('unavailable')
            else:
                row.append('available')
        # End inner loop
                
        # Add the row to the main list
        spots.append(row)
    # End outer loop 
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

# Define named constants.
HEIGHT = 600    # height of the window
WIDTH = 800     # width of the window
ROWS = 6        # number of rows
COLS = 12       # number of columns (6 in left section, 6 in right section)
CELL = 55       # size of each spot cell
GAP = 40        # vertical gap between row pairs
LEFT_X = 40     # x start of left section (A-F)
RIGHT_X = 430   # x start of right section (G-L)
TOP_Y = 520     # y start of top row

# The main program.

# Ask user for check-in time and validating it.
print('Welcome to the Utopia Parking Availability Visualizer!\n')
print('Please enter the check-in time to see parking availability')
while True:
    try:
        check_in_hour = int(input(">> Enter check-in hour (0-23): "))
        if  0 <= check_in_hour <= 23:
            break
        print("** Invalid input. Please enter a time between 0 and 23.")
    except ValueError:
        # Exception if input is not an integer.
        print("** Invalid input. Enter a number")  
         
# Calculating availability based on check-in time.
availability = 0
if (check_in_hour > 0 and check_in_hour <= 6) or (check_in_hour >= 18 and check_in_hour <=23):
    availability = 80
elif check_in_hour >= 7 and check_in_hour <= 11:
    availability = 20
elif check_in_hour >= 12 and check_in_hour <= 17:
    availability = 50
   
# Ask user for background colour and validating the given colour.

print('Choose a background colour (lightgrey, skyblue, yellow).')
bg_colour = "invalid"

while (bg_colour not in ["lightgrey", "skyblue", "yellow"]):
    bg_colour = input(">> Background colour [default: lightgrey]: ") or "lightgrey"
    if bg_colour not in ["lightgrey", "skyblue", "yellow"]:
        print("** Invalid colour. Please choose lightgrey, skyblue or yellow.")

# Ask user for unavailable spot colour and validating the given colour.
print('Choose an unavailable spot colour (red, green, blue).')
unavail_spot_colour = "invalid"

while (unavail_spot_colour not in ["red", "green", "blue"]):
    unavail_spot_colour = input(">> Enter unavailable spot colour [Default: red]: ") or "red"
    if unavail_spot_colour not in ["red", "green", "blue"]:
        print("** Invalid colour. Please choose red, green or blue.")
print("Average parking availability: ",availability,"%")
availability_percent = availability / 100

# Generate Two dimensional list of parking spots
spots = generate_spots(ROWS, COLS, availability_percent)

# Draw with turtle
screen = turtle.Screen()
screen.bgcolor(bg_colour)
screen.setup(WIDTH, HEIGHT)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT) # Set the screen coordinate system from (0,0) to (WIDTH, HEIGHT).
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw parking spots
for row in range(ROWS):
    y = TOP_Y - row * CELL - (row // 2) * GAP
    for col in range(COLS):
        x = LEFT_X + col * CELL if col < (COLS // 2) else RIGHT_X + (col - COLS // 2) * CELL
        draw_square(t, x, y, CELL, unavail_spot_colour if spots[row][col] == "unavailable"  else "white")

# Row numbers between sections
for row in range(ROWS):
    y = TOP_Y - row * CELL - (row // 2) * GAP + CELL // 3
    t.penup()
    t.goto(400, y)
    t.write(ROWS - row, align="center", font=("Arial", 14, "bold"))

# Column letters - below the grid - left section
BOTTOM_Y = TOP_Y - (ROWS - 1) * CELL - ((ROWS - 1) // 2) * GAP - 35
CODE_A = 65
for i in range(6):
    t.penup()
    t.goto(LEFT_X + i * CELL + CELL // 2, BOTTOM_Y)
    letter = chr(CODE_A + i)
    t.write(letter, align="center", font=("Arial", 14, "bold"))

# Column letters - below the grid - right section
for i in range(6):
    t.penup()
    t.goto(RIGHT_X + i * CELL + CELL // 2, BOTTOM_Y)
    letter = chr(CODE_A + ROWS + i)
    t.write(letter, align="center", font=("Arial", 14, "bold"))

# Legend for Available
draw_square(t, 40, 22, 28, "white")
t.penup()
t.goto(76, 29)
t.write("Available", font=("Arial", 12, "normal"))

# Legend for Unavailable
draw_square(t, 210, 22, 28, unavail_spot_colour)
t.penup()
t.goto(246, 29)
t.write("Unavailable", font=("Arial", 12, "normal"))

turtle.done()