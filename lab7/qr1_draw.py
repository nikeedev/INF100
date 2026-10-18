def draw_qr(canvas, x_left, y_top, size, qr):
    for i in range(len(qr)):
        for j in range(len(qr[i])):
            width = size/len(qr)
            height = size/len(qr[i])

            x1_i = x_left + width * j
            x2_i = x1_i + width

            y1_i = y_top + height * i
            y2_i = y1_i + height

            canvas.create_rectangle(x1_i, y1_i, x2_i, y2_i, fill = "black" if qr[i][j] == 1 else "white", outline="")
 

def display(matrix):
    from uib_inf100_graphics.simple import canvas, display as dsp
    canvas.create_rectangle(0, 0, 400, 400, fill='#9bfab4', outline='')
    canvas.create_rectangle(0, 0, 400, 400, fill='white', outline='')
    draw_qr(canvas, 25, 25, 350, matrix)
    dsp(canvas)

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    display(sample_grid)
