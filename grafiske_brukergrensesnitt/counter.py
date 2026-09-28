from uib_inf100_graphics.event_app import run_app
from face import draw_face_at

def app_started(app):   
    # app_started er en "magisk" funksjon som kjører én gang:
    # når programmet starter. Hensikten er å opprette variabler
    app.counter = 0

def key_pressed(app, event):
    # key_pressed er en "magisk" funksjon som kalles hver gang
    # noen trykker på en tast
    app.counter += 1

def redraw_all(app, canvas):
    # redraw_all er en "magisk" funksjon som kalles hver gang
    # skjermen må tegnes på nytt
    cx = app.width / 2
    cy = app.height / 2

    canvas.create_text(cx, cy, text=f"{app.counter}", font="Arial 30")

run_app(width=200, height=100)
