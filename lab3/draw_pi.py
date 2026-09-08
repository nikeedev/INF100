from uib_inf100_graphics.simple import canvas, display
import random
from math import sqrt

def draw_dot(canvas, x, y, color):
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=color)

# Draw a circle in the window
canvas.create_oval(0, 0, 400, 400)

points_inside = 0
color = ""

n = 1000

# Highlight n random points on 400x400 canvas
for _ in range(n):
    x = random.random() * 400
    y = random.random() * 400

    if sqrt((x - 200)**2 + (y - 200)**2) <= 200:
        color = "orange"
        points_inside += 1
    else:
        color = "grey"

    draw_dot(canvas, x, y, color)

our_pi = (points_inside/n) * 4

message = f'{points_inside}/{n} prikker traff sirkelen'
canvas.create_rectangle(80, 180, 320, 220, fill='white')
canvas.create_text(200, 190, text=message, fill='black')

message = f'Beregnet pi: {our_pi}'
canvas.create_text(200, 205, text=message, fill='black')

display(canvas)
