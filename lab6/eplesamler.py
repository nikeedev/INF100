import random

from uib_inf100_graphics.event_app import run_app

from face import draw_face_at


################
###   MODEL  ###
################

def app_started(app):
    app.timer_delay = 1000//60 # 1000 millisekunder / 60 bilder
    app.pressed_keys = []

    app.player = {
        'x': app.width/2,
        'y': app.height - 50,
        'radius': 30
    }
    app.apples = [
        { 'x': app.width / 2, 'y': 0, 'radius': 40},
        { 'x': 100, 'y': 0, 'radius': 30},
    ]
    app.score = 0
    app.state = 'active'
    app.apple_count = len(app.apples)
    app.max_apples = 50


###################
### CONTROLLERS ###
###################

def key_pressed(app, event):
    app.pressed_keys.append(event.key)


def key_released(app, event):
    while event.key in app.pressed_keys:
        app.pressed_keys.remove(event.key)


def move_player(app):
    if 'Left' in app.pressed_keys:
        app.player['x'] -= 10
    elif 'Right' in app.pressed_keys:
        app.player['x'] += 10

def move_apples(app):
    for apple in app.apples:
        apple['y'] += 5


def catch_apples(app):
    # Spise epler
    apples_to_keep = []
    for apple in app.apples:
        if overlaps(app.player, apple):
            app.score += 1
        else:
            apples_to_keep.append(apple)
    app.apples = apples_to_keep

def create_apples(app):
    # Opprette nye epler
    dice_throw = random.random() # flyttall mellom 0.0 og 1.0
    threshold = 0.1 # 10%
    if dice_throw < threshold and app.apple_count < app.max_apples:
        new_apple = {
            'x': random.randrange(app.width),
            'y': 0,
            'radius': random.randrange(20, 50)
        }
        app.apples.append(new_apple)
        app.apple_count += 1

def remove_apples_below_screen(app):
    # Fjern epler fra listen av epler hvis det faller nedenfor skjermbildet 
    remaining_apples = []
    for apple in app.apples:
        if apple['y'] - apple['radius'] >= app.height:
            ...
        else:
            remaining_apples.append(apple)
    app.apples = remaining_apples


def check_game_over(app):
    # Når maks antall epler er opprettet, 
    # OG det ikke er flere epler igjen: sett game_state til ‘game_over’
    if app.apple_count >= app.max_apples and len(app.apples) == 0:
        app.state = 'game_over'


def timer_fired(app):
    move_player(app)
    move_apples(app)
    catch_apples(app)
    create_apples(app)
    remove_apples_below_screen(app)
    check_game_over(app)   
        

def overlaps(c1, c2):
    ''' Returns True if circle c1 overlaps circle c2.
    A circle is a dict with keys x, y and radius'''

    distance = ((c1['x'] - c2['x'])**2 + (c1['y'] - c2['y'])**2)**0.5
    return distance < c1['radius'] + c2['radius']


################
###   VIEW   ###
################

def redraw_all(app, canvas):
    if app.state == 'active':
        redraw_all_active(app, canvas)
    elif app.state == 'game_over':
        redraw_all_game_over(app, canvas)


def redraw_all_active(app, canvas):
    # Draw player
    draw_face_at(canvas, app.player['x'], app.player['y'], app.player['radius'])

    # Draw apple
    for apple in app.apples:
        draw_apple(canvas, apple)

    # Draw score
    canvas.create_text(app.width / 2, 30,
                       text=app.score, font='Arial 30')


def draw_apple(canvas, apple):
    x_lft = apple['x'] - apple['radius']
    x_rgt = apple['x'] + apple['radius']
    y_top = apple['y'] - apple['radius']
    y_bot = apple['y'] + apple['radius']
    canvas.create_oval(x_lft, y_top, x_rgt, y_bot, fill='red')


def redraw_all_game_over(app, canvas):
    canvas.create_text(app.width/2, app.height/2, 
                       text=('Game Over\nYour score is '
                             f'{app.score}/{app.max_apples} points'),
                       font='Arial 30')
    

if __name__ == '__main__':
    run_app(width=600, height=600, title='eplesamler')
