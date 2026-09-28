from uib_inf100_graphics.event_app import run_app
from face import draw_face_at
import random

def app_started(app):
    app.xc = 300
    app.yc = 300
    app.radius = 200
    app.score = 0

def mouse_pressed(app, event):
    app.xc = random.randrange(app.width)
    app.yc = random.randrange(app.height)
    
    if click_is_within_face(app, event):
        app.score += 1
    else:
        app.score -= 1

def click_is_within_face(app, event):
    distance_from-center = 
    return distance_from_center <= app.radius

def redraw_all(app, canvas):
    draw_face_at(canvas, app.xc, app.yc, app.radius)
    canvas.create_text(app.width/2, app.height - 20, text=app.score, font="Arial 30")

run_app(width=600, height=600)
