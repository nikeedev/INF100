from uib_inf100_graphics.event_app import run_app
from face import draw_face_at

import random

fps = 72

def app_started(app):
    app.timer_delay = 1000//fps

    app.player = {
        "x": app.width/2,
        "y": app.height - 50,
        "r": 20
    }

    """
    app.apple = {
        "x": app.width/2,
        "y": 0,
        "r": 10
    }
    """

    app.score = 0
    
    app.apples = []
    for _ in range(2):
        app.apples.append({
            "x": random.randrange(20, app.width - 20),
            "y": 0,
            "r": 10
        })

    app.pressed_keys = []


def key_pressed(app, event):
    app.pressed_keys.append(event.key) 

def key_released(app, event):
    while event.key in app.pressed_keys:
        app.pressed_keys.remove(event.key)

def circles_overlap(x1, y1, r1, x2, y2, r2):
    d = (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2)

    return d <= (r1+r2)

def overlaps(player, apple):
    return circles_overlap(player["x"], player["y"], player["r"], apple["x"], apple["y"], apple["r"])

def timer_fired(app):
    if "Right" in app.pressed_keys and app.player["x"] <= app.width - app.player["r"]:
        app.player["x"] += 10
    if "Left" in app.pressed_keys and app.player["x"] >= app.player["r"]:
        app.player["x"] -= 10
    
    apples_to_keep = []
    for apple in app.apples:
        apple["y"] += 5
        
        if overlaps(app.player, apple):
            app.score += 1
        else:
            apples_to_keep.append(apple)
    
    app.apples = apples_to_keep

    dice_throw = random.random()
    threshold = 0.1 # 10%
    if dice_throw < 0.1:
        new_apple = {
            "x": random.randrange(app.width),
            "y": 0,
            "r": random.randrange(20, 50)
        }
        app.apples.append(new_apple)
    

def draw_apple(canvas, apple):
    x_left = apple["x"] - apple["r"]
    x_right = apple["x"] + apple["r"]   
    y_top = apple["y"] - apple["r"]
    y_bottom = apple["y"] + apple["r"]

    canvas.create_oval(x_left, y_top, x_right, y_bottom, fill="red")

def redraw_all(app, canvas):
    draw_face_at(canvas, app.player["x"], app.player["y"], app.player["r"])
    
    for apple in app.apples:
        draw_apple(canvas, apple)

    canvas.create_text(app.width/2, 20, text=f"Score: {app.score}", anchor='center', font="Arial 10")

run_app(width=500, height=500, title="Eplesamleren")

