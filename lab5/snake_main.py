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
    return (pos[0] > len(board) or pos[1] > len(board)) or (pos[0] < 0 or pos[1] < 0)

def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos, app.direction)
    
    if is_legal_move(app.head_pos, app.board):
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
    app.info_mode = True
    app.score = 0

    app.state = "active"

    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    app.snake_size = 3
    app.head_pos = (3, 4)

#def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    
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
        if event.key == "Space":
            move_snake(app)
        
    if event.key == "Escape":
        exit(0)

    if event.key == "i":
        app.info_mode = not app.info_mode
     
def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
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

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app

    run_app(width=500, height=400, title='Snake')


