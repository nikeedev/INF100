from math import sqrt

def rectangles_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    r1_left = min(x1, x2)
    r1_right = max(x1, x2)
    r1_top = min(y1, y2)
    r1_bottom = max(y1, y2)

    r2_left = min(x3, x4)
    r2_right = max(x3, x4)
    r2_top = min(y3, y4)
    r2_bottom = max(y3, y4)

    # return (r1_bottom >= r2_top or r1_right <= r2_left) and (r2_bottom >= r1_top or r2_right >= r1_left)
    
    return (r1_right >= r2_left or r2_right <= r1_left) and (r1_bottom >= r2_top or r2_bottom <= r1_top)

def test_rectangles_overlap():
    print('Tester rectangles_overlap... ', end='')
    assert rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6) is True # Delvis overlapp
    assert rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4) is True # Fullstendig overlapp
    assert rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7) is True # Kryssende rektangler
    assert rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7) is True # Deler et hjørne
    assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False # Utenfor
    assert rectangles_overlap(1, 1, 2, 2, 3, 3, 4, 4) is False
    print('OK')

test_rectangles_overlap()

#################################################
##################   Del B   ####################
#################################################
#################################################


def point_in_rectangle(x1, y1, x2, y2, xp, yp):
    x_left = min(x1, x2)
    x_right = max(x1, x2)
    y_top = min(y1, y2)
    y_bottom = max(y1, y2)
    
    return (xp >= x_left and yp >= y_top) and (xp <= x_right and yp <= y_bottom)

def distance(x, y, xc, yc):
    d = sqrt(abs(xc-x)**2 + abs(yc-y)**2)
    return d


def circle_overlaps_rectangle(x1, y1, x2, y2, xc, yc, rc):
    x_left = min(x1, x2)
    x_right = max(x1, x2)
    y_top = min(y1, y2)  
    y_bottom = max(y1, y2) 

    x1_utvidet = x_left - rc
    x2_utvidet = x_right + rc
    y1_utvidet = y_top - rc  
    y2_utvidet = y_bottom + rc 


    if point_in_rectangle(x1, y1, x2, y2, xc, yc):
        return True

    elif not point_in_rectangle(x1_utvidet, y1_utvidet, x2_utvidet, y2_utvidet, xc, yc):
        return False
    
    elif x_left <= xc <= x_right:
        return True
    elif y_top <= yc <= y_bottom:
        return True
    
    elif distance(x1, y1, xc, yc) <= rc:
        return True
    elif distance(x2, y1, xc, yc) <= rc:
        return True
    elif distance(x1, y2, xc, yc) <= rc:
        return True 
    elif distance(x2, y2, xc, yc) <= rc:
        return True
    
    else:
        return False


def test_circle_overlaps_rectangle():
    print('Tester circle_overlaps_rectangle... ', end='')
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2) is True # på midten
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01) is True # på kanten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2) is False # langt utenfor
    assert circle_overlaps_rectangle(0, 5, 5, 0, 5.1, 5.1, 1) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5) is False # bare nesten
    print('OK')


test_circle_overlaps_rectangle()
