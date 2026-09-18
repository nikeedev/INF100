from uib_inf100_graphics.simple import canvas, display

def draw_grid(canvas, x1, y1, x2, y2, colors): 
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            width = (x2-x1)/len(colors[i])
            height = (y2-y1)/len(colors)

            x1_i = x1 + width * j
            x2_i = x1_i + width

            y1_i = y1 + height * i
            y2_i = y1_i + height

            canvas.create_rectangle(x1_i, y1_i, x2_i, y2_i, fill = colors[i][j], outline = 'black')

