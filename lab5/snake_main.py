from snake_view import draw_board
from random import randint

def subtract_one_from_all_positives(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 1:
                grid[i][j] -= 1

def get_next_head_position(head_pos, direction):
    head_pos_x = head_pos[1]
    head_pos_y = head_pos[0]

    if direction == "north":
        head_pos_y -= 1
    elif direction == "south":
        head_pos_y += 1
    elif direction == "east":
        head_pos_x += 1
    elif direction == "west":
        head_pos_x -= 1

    return (head_pos_y, head_pos_x)

def add_apple_at_random_location(grid):
    x = 0
    y = 0
    while True:
        x = randint(0, len(grid) - 1)
        y = randint(0, len(grid[0]) - 1)

        if grid[x][y] == 0:
            grid[x][y] = -1
            break;

def is_legal_move(pos, board):
    if (pos[0] < len(board) and pos[1] < len(board[0])) and (pos[0] > -1 and pos[1] > -1):
        if board[pos[0]][pos[1]] <= 0:
            return True
    return False

def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos, app.direction)
    
    if not is_legal_move(app.head_pos, app.board):
        app.state = "gameover"
        return

    if app.board[app.head_pos[0]][app.head_pos[1]] == -1:
        app.snake_size += 1

        app.score += 1
        
        add_apple_at_random_location(app.board)
    else:
        subtract_one_from_all_positives(app.board)
    
    app.board[app.head_pos[0]][app.head_pos[1]] = app.snake_size

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.direction = "east"
    
    try:
        app.info_mode = app.info_mode
    except Exception:
        app.info_mode = False

    app.score = 0
    app.state = "active"


    app.buttons = [
        # [x1, y1, x2, y2, "Navn på knapp", scene, funksjon]
        [app.width/2 - 100, app.height/2 + 25, app.width/2 + 100, app.height/2 + 125, "Retry?", "gameover", retry],
        [app.width/4, app.height/2 + 160, app.width/4 + 50, app.height/2 + 260, "Back to menu", "gameover", back_to_menu],
        [app.width/4 * 3, app.height/2 + 150, app.width/4 * 3 + 50, app.height/2 + 210, "Play", "menu", play]
    ]

    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    app.snake_size = 3
    app.head_pos = (3, 4)
    app.timer_delay = 200


def retry(app):
    app_started(app)

def back_to_menu(app):
    app.state = "menu"

def play(app):
    app_started(app)


def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.

    if not app.info_mode and app.state == "active":
        move_snake(app)

def point_in_rectangle(x1, y1, x2, y2, x, y):
    return (min(x1, x2) <= x <= max(x1, x2)
        and min(y1, y2) <= y <= max(y1, y2))

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    
    if app.state == "active":
        if event.key == "Up" or event.key == "w":
            app.direction = "north"
        elif event.key == "Left" or event.key == "a":
            app.direction = "west"
        elif event.key == "Down" or event.key == "s":
            app.direction = "south"
        elif event.key == "Right" or event.key == "d":
            app.direction = "east"

        if event.key == "Space" and app.info_mode:
            move_snake(app)
      
    if event.key == "Escape":
        exit(0)

    if event.key == "i":
        app.info_mode = not app.info_mode

    if event.key == "r" and not app.state == "menu":
        app_started(app)

def execute_button_action_if_clicked(app, button, mouse_x, mouse_y):
    x1, y1, x2, y2, label, scene, func = button

    print(scene)
    if point_in_rectangle(x1, y1, x2, y2, mouse_x, mouse_y) and app.state == scene:
        func(app)

def mouse_pressed(app, event):
    for button in app.buttons:
        x1, y1, x2, y2, label, scene, func = button
        if scene == app.state:
            execute_button_action_if_clicked(app, button, event.x, event.y)

def draw_button(app, canvas, button):
    x1, y1, x2, y2, output, scene, func = button
    if app.state == scene:
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray")
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        if type(output) == str:
            canvas.create_text(mid_x, mid_y, text=output)
        else:
            canvas.create_image(mid_x, mid_y, pil_image=image)


def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    
    if app.state == "active":
        if app.info_mode:
            canvas.create_text(
                    app.width/2, 
                    11, 
                    text=f"{app.head_pos=} {app.snake_size=} {app.direction=}", 
                    anchor='center', 
                    font='Arial 10'
            )
        else:
            canvas.create_text(app.width/2, 11, text=f"Score: {app.score}", anchor='center', font='Arial 10')
            
        draw_board(canvas, 25, 25, app.width - 25, app.height-25, app.board, app.info_mode)

    elif app.state == "gameover":
        canvas.create_text(app.width/2, app.height/2 - 100, text="Game over", anchor='center', font='Arial 50')
        canvas.create_text(app.width/2, app.height/2 + 11, text=f"Score: {app.score}", anchor='center', font='Arial 20')
     
    elif app.state == "menu":
        canvas.create_text(app.width/2, app.height/2 - 100, text="Snake", anchor='center', font='Arial 50', fill="green")

    for button in app.buttons:
        draw_button(app, canvas, button)
        

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app

    run_app(width=500, height=400, title='Snake')


