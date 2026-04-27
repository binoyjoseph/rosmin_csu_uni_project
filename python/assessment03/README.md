## Coordinate System

screen.setworldcoordinates(0, 0, WIDTH, HEIGHT) sets up the window so:

- (0, 0) is the bottom-left
- (800, 600) is the top-right
- X increases rightward, Y increases upward

## Window & Grid Constants

| Constant | Value | Meaning                                                  |
|----------|-------|----------------------------------------------------------|
| WIDTH    | 800   | Window width in pixels                                   |
| HEIGHT   | 600   | Window height in pixels                                  |
| CELL     | 55    | Width and height of each square spot                     |
| GAP      | 40    | Extra vertical space inserted between every pair of rows |
| LEFT_X   | 40    | Left edge of the left section (columns A–F)              |
| RIGHT_X  | 430   | Left edge of the right section (columns G–L)             |
| TOP_Y    | 520   | Y position of the top row (row 0)                        |


## Spot Grid — X Position (main.py:98)

x = LEFT_X + col * CELL           # cols 0–5  → left section
x = RIGHT_X + (col - COLS//2) * CELL  # cols 6–11 → right section
Columns 0–5 start at LEFT_X = 40 and step right by CELL = 55 each time.
e.g. col 0 → x=40, col 1 → x=95, col 5 → x=315
Columns 6–11 mirror the same logic but start at RIGHT_X = 430, with the index offset back to 0–5.
e.g. col 6 → x=430, col 11 → x=705
The gap between x=315+55=370 and x=430 is 60px — the visual aisle between the two sections.
Spot Grid — Y Position (main.py:96)

y = TOP_Y - row * CELL - (row // 2) * GAP
row * CELL steps downward by 55px for each row.
(row // 2) * GAP inserts an extra 40px gap after every pair of rows, creating three visual row-groups (rows 0–1, 2–3, 4–5).
Row 0 starts at TOP_Y = 520. Each row goes further down:

| Row | row*CELL | (row//2)*GAP | Y   |
|-----|----------|--------------|-----|
| 0   | 0        | 0            | 520 |
| 1   | 55       | 0            | 465 |
| 2   | 110      | 40           | 370 |
| 3   | 165      | 40           | 315 |
| 4   | 220      | 80           | 220 |
| 5   | 275      | 80           | 165 |


## Row Numbers (main.py:103)

y = TOP_Y - row * CELL - (row // 2) * GAP + CELL // 3
Same formula as the spot Y, plus CELL // 3 = 18px to vertically centre the number inside the square. They're drawn at x = 400, which sits in the aisle between the two sections.

## Column Letters (main.py:109)

BOTTOM_Y = TOP_Y - (ROWS - 1) * CELL - ((ROWS - 1) // 2) * GAP - 35
This computes the Y of row 5 (the last row) and subtracts 35px more to place the letters just below the bottom edge of the squares.

The X for each letter is LEFT_X + i * CELL + CELL // 2 — the same column X as the spot, plus half a cell to centre the letter horizontally over the square.

## Legend (main.py:125–133)
The legend squares are hardcoded near the bottom of the window at y = 22 (squares) and y = 29 (text labels), well below the grid which ends at y=165.