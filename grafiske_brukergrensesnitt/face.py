def draw_face_fixed(canvas):
    canvas.create_oval(0, 0, 400, 400, fill="pink")    
    
    canvas.create_oval(120, 110, 150, 190, fill="red")
    canvas.create_oval(240, 110, 270, 190, fill="red")
    
    canvas.create_line(115, 300, 200, 360, 285, 300, fill="red", width=6, smooth=True)

def draw_face_scaled(canvas, width, height):
    diff_x = width  / 400
    diff_y = height / 400
    
    canvas.create_oval(0, 0, 400 * diff_x, 400 * diff_y, fill="pink")    
    
    canvas.create_oval(120 * diff_x, 110 * diff_y, 150 * diff_x, 190 * diff_y, fill="red")
    canvas.create_oval(240 * diff_x, 110 * diff_y, 270 * diff_x, 190 * diff_y, fill="red")
    
    canvas.create_line(115 * diff_x, 300 * diff_y, 200 * diff_x, 360 * diff_y, 285 * diff_x, 300 * diff_y, fill="red", width=round(6 * diff_x), smooth=True)



def draw_face_shifted(canvas, x_lft, y_top, width, height):
    diff_x = width  / 400
    diff_y = height / 400
    
    canvas.create_oval(x_lft, y_top, 400 * diff_x + x_lft, 400 * diff_y + y_top, fill="pink")    
    
    canvas.create_oval(120 * diff_x + x_lft, 110 * diff_y + y_top, 150 * diff_x + x_lft, 190 * diff_y + y_top, fill="red")
    canvas.create_oval(240 * diff_x + x_lft, 110 * diff_y + y_top, 270 * diff_x + x_lft, 190 * diff_y + y_top, fill="red")
    
    canvas.create_line(115 * diff_x + x_lft, 300 * diff_y + y_top, 200 * diff_x + x_lft, 360 * diff_y + y_top, 285 * diff_x + x_lft, 300 * diff_y + y_top, fill="red", width=6, smooth=True)


def draw_face_at(canvas, x_center, y_center, radius):
    x_lft = x_center - radius
    y_top = y_center - radius
    width = 2 * radius
    height = 2 * radius
    
    draw_face_shifted(canvas, x_lft, y_top, width, height)



