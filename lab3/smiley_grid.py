# smiley_grid.py
from smiley import draw_smiley


def main():
    from uib_inf100_graphics.simple import canvas, display
    draw_smiley_grid(canvas, 70, 5)
    display(canvas)


def draw_smiley_grid(canvas, size, n):
    for i in range(0, n):
        for j in range(0, n):
            draw_smiley(canvas, i*size, j*size, size)



def draw_smiley_line(canvas, y, size, n):
    for i in range(0, n):
        draw_smiley(canvas, i*size, y, size)

if __name__ == '__main__':
    main()


