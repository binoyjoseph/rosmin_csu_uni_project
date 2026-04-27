## Logic

The question says to draw the parking spots in an 800x600 px layout.

```screen.setworldcoordinates(0, 0, 800, 600)```

This makes (0, 0) the bottom-left corner and (800, 600) the top-right. So x increases going right, y increases going up — all values are positive.

---

`CELL = 55` — each spot is a 55×55 square. This drives everything else.

Layout math:
- CELL = 55, two sections of 6×55 = 330px each + 60px gap = 720px total chart width
- Centering: (800 − 720) / 2 = 40px padding each side → LEFT_X = 40, RIGHT_X = 430

LEFT_X = 40 — where the left section (A–F) starts
The total chart width is: 2 sections × 6 cells + gap = 12×55 + 60 = 720px
Centering it on an 800px canvas: (800 − 720) / 2 = 40px of padding on each side.
So the left section starts at x = 40.

RIGHT_X = 430 — where the right section (G–L) starts
Left section ends at: 40 + 6×55 = 370
Then a 60px gap (for the row number labels): 370 + 60 = 430
Right section then ends at: 430 + 6×55 = 760, leaving 40px padding on the right. Perfectly symmetric.


The coordinate system

setworldcoordinates(0, 0, 800, 600) puts (0,0) at the bottom-left and (800,600) at the top-right. All coordinates are positive.

Horizontal (x-axis)

The total chart width is 12 cells × 55px + 60px gap = 720px.
Centering on an 800px canvas: (800 − 720) / 2 = 40px padding each side.


x=0    x=40          x=370  x=400  x=430          x=760   x=800
|  40px |  A–F (330px)  | gap |  G–L (330px)  |  40px  |
LEFT_X = 40 — left section starts 40px from the left edge
RIGHT_X = 430 — 40 + 330 + 60 = 430, where the 60px gap holds the row number labels centred at x=400
Right section ends at 430 + 330 = 760, leaving 40px on the right — symmetric with the left
Vertical (y-axis)

The chart height is 6 rows × 55px + 2 gaps × 40px = 330 + 80 = 410px.


y=600   ← top edge
y=540   ← top of chart        (60px top space)
  ...     row 6
  ...     GAP (40px)
  ...     row 5 / row 4
  ...     GAP (40px)
  ...     row 3 / row 2
  ...     row 1
y=130   ← BASE_Y (bottom of chart)
y=95    ← column letters       (BASE_Y − 35)
y=22    ← legend squares
y=0     ← bottom edge
BASE_Y = 130 — chosen so the top of the chart lands at 130 + 410 = 540, leaving exactly 60px at the top
Column letters sit at BASE_Y − 35 = 95, 35px below the grid
Legend is fixed at y=22, giving 22px of breathing room from the bottom edge
The gap formula (row // 2 * GAP)

Rows are drawn in pairs. row // 2 gives the pair index (0, 0, 1, 1, 2, 2), so the extra y-offset added per row is:

Row index	Pair	Gap offset
0, 1	0	0px
2, 3	1	40px
4, 5	2	80px
This pushes each pair further up, creating the visible space between them.


| Element       | Value | Reasoning                                              |
|---------------|-------|--------------------------------------------------------|
| LEFT_X = 40   | x=40  | (800 − 720) / 2 = 40px padding each side               |
| RIGHT_X = 430 | x=430 | 40 + 6×55 + 60px gap = 430                             |
| Right edge    | x=760 | 430 + 6×55 = 760, leaving 40px right padding           |
| BASE_Y = 100  | y=100 | leaves 100px below for labels (y=65) and legend (y=22) |
| Row labels    | x=400 | midpoint of the 60px gap between sections              |
| Top of chart  | y=470 | 100 + 6×55 + 2×20 = 470, leaving 130px top padding     |

The smallest coordinate in the file is y=22 (legend square).