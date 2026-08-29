# belgian_flag.py

def draw_belgian_flag(canvas, x1, y1, x2, y2):
    total_width = (x2-x1)/3

    x1_b = x1
    x2_b = x1_b + total_width

    x1_y = x2_b
    x2_y = x1_y + total_width  
   
    x1_r = x2_y 
    x2_r = x1_r + total_width


    canvas.create_rectangle(x1_b, y1, x2_b, y2, fill = 'black', outline = '')
    canvas.create_rectangle(x1_y, y1, x2_y, y2, fill = 'yellow', outline = '')
    canvas.create_rectangle(x1_r, y1, x2_r, y2, fill = 'red', outline = '')


