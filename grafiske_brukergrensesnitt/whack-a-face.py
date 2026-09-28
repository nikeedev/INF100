from uib_inf100_graphics.event_app import run_app
from face import draw_face_at
import random
from math import sqrt

def app_started(app):
    app.xc = 300
    app.yc = 300
    app.radius = 200
    app.score = 0

def mouse_pressed(app, event):
    if click_is_within_face(app, event):
        app.score += 1
    else:
        app.score -= 1

    app.xc = random.randrange(app.width)
    app.yc = random.randrange(app.height)

def click_is_within_face(app, event):
    distance_from_center = sqrt((event.x - app.xc) ** 2 + (event.y - app.yc) ** 2)
    print(f"x({app.xc}, {app.yc}) and event({event.x}, {event.y}) distance from center: {distance_from_center}, app radius: {app.radius} (distance_from_center <= app.radius: {distance_from_center <= app.radius})")
    return distance_from_center <= app.radius

def redraw_all(app, canvas):
    draw_face_at(canvas, app.xc, app.yc, app.radius)
    canvas.create_text(app.width/2, app.height - 20, text=app.score, font="Arial 30")

run_app(width=600, height=600)
