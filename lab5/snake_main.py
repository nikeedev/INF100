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
        
        #if app.score > app.highscore:
        #    app.highscore = app.score

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
    app.state = "menu"

    # Kilde til knapper: https://inf100.ii.uib.no/notat/gui/#eksempel-knapper 
    app.buttons = [
        # [x1, y1, x2, y2, "Navn på knapp", scene, funksjon]
        # gameover screen
        [app.width/2 - 50, 260, app.width/2 + 50, 290, "Retry?", "gameover", retry],
        [app.width/2 - 100, 310, app.width/2 + 100, 340, "Back to menu", "gameover", back_to_menu],

        # how-to menu
        [app.width/2 - 100, app.height - 60, app.width/2 + 100, app.height - 10, "Back to menu", "how", back_to_menu],
        
        # Game menu
        [app.width/2 - 25, app.height/2 - 50 , app.width/2 + 25, app.height/2, "Play", "menu", play],
        [app.width/2 - 100, app.height/2 + 100, app.width/2 + 100, app.height/2 + 50, "How to play?", "menu", how_to]
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


    app.highscore = 0

def reset(app):
    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
     
    app.direction = "east"
    app.snake_size = 3
    app.head_pos = (3, 4)
    
    if app.score > app.highscore:
        app.highscore = app.score

    app.score = 0
    app.state = "active"

def retry(app):
    reset(app) 

def back_to_menu(app):
    app.state = "menu"

def play(app):
    reset(app)

def how_to(app):
    app.state = "how"

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
        x, y = app.head_pos
        if (event.key == "Up" or event.key == "w") and not app.direction == "south":
            app.direction = "north"
        elif (event.key == "Left" or event.key == "a") and not app.direction == "east":
            app.direction = "west"
        elif (event.key == "Down" or event.key == "s") and not app.direction == "north":
            app.direction = "south"
        elif (event.key == "Right" or event.key == "d") and not app.direction == "west":
            app.direction = "east"

        if event.key == "Space" and app.info_mode:
            move_snake(app)
    
    elif app.state == "menu":
        if event.key == "Space":
            reset(app)


    if event.key == "Escape":
        exit(0)

    if event.key == "i":
        app.info_mode = not app.info_mode

    if event.key == "r" and not app.state == "menu":
        reset(app)


#######
# Gjenbruk av kilder i fra linje 75:
# Kilde: https://inf100.ii.uib.no/notat/gui/#eksempel-knapper
#####

def execute_button_action_if_clicked(app, button, mouse_x, mouse_y):
    x1, y1, x2, y2, label, scene, func = button

    # print(scene)
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
            canvas.create_text(mid_x, mid_y, text=output, font="Arial 15")
        else:
            canvas.create_image(mid_x, mid_y, pil_image=image)

##
#####
######

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
            canvas.create_text(app.width/4, 11, text=f"Score: {app.score}", anchor='center', font='Arial 10', fill="green" if app.score > app.highscore else "black")
            canvas.create_text(app.width*(3/4), 11, text=f"High score to beat: {app.highscore}", anchor='center', font='Arial 10')

        draw_board(canvas, 25, 25, app.width - 25, app.height-25, app.board, app.info_mode)

    elif app.state == "gameover":
        canvas.create_text(app.width/2, 50, text="Game over", anchor='center', font='Arial 50')

        if app.score > app.highscore:
            canvas.create_text(app.width/2, 170, text=f"New high score: {app.score}!", anchor='center', font='Arial 22', fill="green")
        else:
            canvas.create_text(app.width/2, 140, text=f"Score: {app.score}", anchor='center', font='Arial 20')
            canvas.create_text(app.width/2, 170, text=f"High score: {app.highscore}", anchor='center', font='Arial 12')

     
    elif app.state == "menu":
        canvas.create_text(app.width/2, 50, text="Snake", anchor='center', font='Consolas 50 italic', fill="red")

        canvas.create_text(app.width/2, 100, text="Press space to start", anchor='center', font='Consolas 14')

        canvas.create_text(app.width/2, app.height - 20, text="© nikeedev (Nikita Goncarenko) 2026", anchor='center', font='Arial 12')
    
    elif app.state == "how":
        # ← → ↑ ↓ 
        canvas.create_text(app.width/2, 40, text="\"How to play this game??\"", anchor="center", font="Arial 30", fill="green")
        canvas.create_text(app.width/2, 185, text="It is easy :)\n\tUp: ↑ or W\n\tDown: ↓ or S\n\tLeft: ← or A\n\tRight: → or D\n\nPress Space to start the game (at menu)\nPress R to reset the game.\nPress Esc (escape) to close the game completely\n\nIf you are also a good debugging person,\nyou can enable debug mode by pressing I,\nit lets you step through the game loop\nand shows variable stats.", anchor="center", font="Arial 12")
    
    for button in app.buttons:
        draw_button(app, canvas, button)
        

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app

    run_app(width=500, height=400, title='Snake')


