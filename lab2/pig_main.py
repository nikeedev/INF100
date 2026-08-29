# pig_main.py
from uib_inf100_graphics.simple import canvas, display
from pig_head import draw_head
from pig_body import draw_body

draw_body(canvas, 50, 100, 350, 300)
draw_head(canvas, 300, 100, 60)

display(canvas)
