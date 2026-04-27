## Coordinate System

setworldcoordinates(0, 0, WIDTH, HEIGHT)

- set (0, 0) as the bottom-left
- (800, 600) as the top-right
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

```
y = TOP_Y - row * CELL - (row // 2) * GAP + CELL // 3
t.write(ROWS - row, ...)
```

Identical Y formula to the spots, plus CELL // 3 = 18px to vertically centre the number inside the square. ROWS - row reverses the label so the top square (row index 0) shows 6 and the bottom square (row index 5) shows 1, giving a bottom-to-top numbering. Drawn at x = 400, sitting in the aisle between sections.

## Column Letters (main.py:109)

```
BOTTOM_Y = TOP_Y - (ROWS - 1) * CELL - ((ROWS - 1) // 2) * GAP - 35
```

This computes the Y of the last row (row index 5 → y=165) then subtracts 35 more, placing the letters at y=130, just below the bottom edge of the grid. Each letter's X is LEFT_X + i * CELL + CELL // 2 (or the right-section equivalent) — the column's X position plus half a cell to centre the letter horizontally over its square.

## Legend (main.py:125–133)
Hardcoded at y = 22 (squares) and y = 29 (text), near the very bottom of the window. These sit well below the grid (which ends at y=165) in the spare space beneath it.