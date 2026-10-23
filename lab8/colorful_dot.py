from uib_inf100_graphics.event_app import run_app

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def app_started(app):
    app.r = 100
    app.g = 149
    app.b = 237
    app.radius = 60
    app.text = "Trykk på piltastene og a,z for å endre fargen"

    app.modes = [1, 10, 20, 50]
    
    app.increase = 1
    
def key_pressed(app, event):
    if event.key == "Space":
        if app.modes.index(app.increase) + 1 > len(app.modes) - 1:
            app.increase = app.modes[0]
        else:
            app.increase = app.modes[app.modes.index(app.increase) + 1]

    elif event.key == "Up":
        app.r += app.increase  
    elif event.key == "Down":
        app.r -= app.increase
   
    elif event.key == "Right":
        app.g += app.increase 
    elif event.key == "Left":
        app.g -= app.increase 

    elif event.key == "a":
        app.b += app.increase
    elif event.key == "z":
        app.b -= app.increase
    
    # slutt programmet
    elif event.key == "q":
        print("'q' har blitt trykket\nAvslutter programmet!")
        exit(0)
    
    # Gå tilbake til 255 og nedover
    if app.r < 0:
        app.r = 255 + app.r

    if app.g < 0:
        app.g = 255 + app.g

    if app.b < 0:
        app.b = 255 + app.b


    # Gå tilbake til 0 og oppover
    if app.r > 255:
        app.r = app.r - 255

    if app.g > 255:
        app.g = app.g - 255

    if app.b > 255:
        app.b = app.b - 255 

    app.text = f"Trykket '{event.key}', fargen er {app.r=} {app.g=} {app.b=}\nModus: Endring med {app.increase}"
    

def redraw_all(app, canvas):
    canvas.create_text(app.width/2, 20, text=app.text, anchor="center")
    canvas.create_oval(app.width/2 - app.radius, app.height/2 - app.radius, app.width/2 + app.radius, app.height/2 + app.radius, fill=rgb_to_hex(app.r, app.g, app.b), outline="")



run_app(width=400, height=300)
