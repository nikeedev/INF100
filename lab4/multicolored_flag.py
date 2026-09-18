from uib_inf100_graphics.simple import canvas, display

def draw_multicolored_flag(canvas, x1, y1, x2, y2, colors):
    width = (x2-x1)/len(colors)

    for i in range(len(colors)):
        x1_i = x1 + width * i
        x2_i = x1_i + width
        
        canvas.create_rectangle(x1_i, y1, x2_i, y2, fill = colors[i], outline = '')

