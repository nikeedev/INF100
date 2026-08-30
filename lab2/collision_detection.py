def rectangles_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    x1_left = min(x1, x2)
    x1_right = max(x1, x2)

    y1_top = min(y1, y2)
    y1_bottom = max(y1, y2)

    x2_left = min(x3, x4)
    x2_right = max(x3, x4)

    y2_top = min(y3, y4)
    y2_bottom = max(y3, y4)

    return (xp >= x_left and yp >= y_top) and (xp <= x_right and yp <= y_bottom)




def test_rectangles_overlap():
    print('Tester rectangles_overlap... ', end='')
    assert rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6) is True # Delvis overlapp
    assert rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4) is True # Fullstendig overlapp
    assert rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7) is True # Kryssende rektangler
    assert rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7) is True # Deler et hjørne
    assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False # Utenfor
    print('OK')

test_rectangles_overlap()
