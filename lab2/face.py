from uib_inf100_graphics.simple import canvas, display
from uib_inf100_graphics.helpers import load_image_http, scaled_image


canvas.create_oval(50, 20, 350, 320, fill="#ebd7af", outline='')

# eyes1
canvas.create_oval(100, 100, 150, 150, fill="white", outline='')
canvas.create_oval(115, 115, 135, 135, fill="#6495ED", outline='')

# eyes2
canvas.create_oval(100 + 150, 100, 150 + 150, 150, fill="white", outline='')
canvas.create_oval(115 + 150, 115, 135 + 150, 135, fill="#6495ED", outline='')

# mouth
canvas.create_polygon(150, 170, 200, 220, 250, 170, smooth=True, fill="black")

image = scaled_image(load_image_http('https://i1.sndcdn.com/artworks-000666620167-6kjqim-t500x500.jpg'), 0.05)

canvas.create_image(270, 350, pil_image=image)

canvas.create_text(300, 350, text = "pog", font=("Courier New", 13, 'bold'))

display(canvas)
