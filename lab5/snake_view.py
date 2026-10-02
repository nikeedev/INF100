from uib_inf100_graphics.helpers import load_image, scaled_image

def get_color(value):
    if value == 0:
        return "lightgray"
    if value >= 1:
        return "orange"
    if value <= -1:
        return "cyan"

def draw_board(canvas, x1, y1, x2, y2, board, info_mode):
    image = scaled_image(load_image('smol_apple.png'), 0.15)

    for i in range(len(board)):
        for j in range(len(board[i])):
            width = (x2-x1)/len(board[i])
            height = (y2-y1)/len(board)

            x1_i = x1 + width * j
            x2_i = x1_i + width

            y1_i = y1 + height * i
            y2_i = y1_i + height

            cell_x_mid = (x1_i + x2_i)/2
            cell_y_mid = (y1_i + y2_i)/2


            if board[i][j] == -1:
                canvas.create_image(cell_x_mid, cell_y_mid, pil_image=image)
            else:
                canvas.create_rectangle(x1_i, y1_i, x2_i, y2_i, fill = get_color(board[i][j]), outline = 'black')
            
            if info_mode:
                canvas.create_text(cell_x_mid, cell_y_mid + 5, text=f"{j}, {i}\n{board[i][j]}", anchor='center', font='Arial 9')


if __name__ == '__main__':
    from uib_inf100_graphics.simple import canvas, display

    test_board = [
        [1, 2, 3, 0, 5, 4,-1,-1, 1, 2, 3],
        [0, 4, 0, 7, 0, 3,-1, 0, 0, 4, 0],
        [0, 5, 0, 8, 1, 2,-1,-1, 0, 5, 0],
        [0, 6, 0, 9, 0, 0, 0,-1, 0, 6, 0],
        [0, 7, 0,10,11,12,-1,-1, 0, 7, 0],
    ]

    draw_board(canvas, 25, 80, 375, 320, test_board, True)

    display(canvas)
