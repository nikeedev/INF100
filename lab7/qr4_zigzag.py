def get_next_pos(row, column, size):
    next_row = row
    next_column = column
    
    if column % 2 == 0:
        if column == 0: 
            next_row -= 1
        else:
            next_column -= 1 

    elif column % 4 == 1:
        if row == size - 1:
            next_column -= 1
        else:
            next_column += 1
            next_row += 1

    else:
        if row == 0:
            next_column -= 1
        else:
            next_column += 1
            next_row -= 1
    
    return (next_row, next_column)

def bit_list_to_raw_matrix(bit_list, qr_layout):
    raw_matrix = []
    size = qr_layout["side_length"]
    
    if len(bit_list) > size**2:
        raise ValueError(f"Lengden til bit_list er lengre enn totalt antall plass i matrisen.")
        
    for i in range(size):
        raw_matrix.append([])
        for j in range(size):
            raw_matrix[i].append(0)
    
    pos = [size - 1, size - 1]
    i = 0

    while i < len(bit_list):
        if not reserved(pos[0], pos[1], qr_layout):
            raw_matrix[pos[0]][pos[1]] = bit_list[i]
            i += 1
                    
        row, column = get_next_pos(pos[0], pos[1], size)
        pos[0] = row
        pos[1] = column

    # print(raw_matrix)

    return raw_matrix

def reserved(row, col, qr_layout):
    reserved = qr_layout["fixed_positions"]["ones"] + qr_layout["fixed_positions"]["zeros"] + qr_layout["meta_positions"]["first"] + qr_layout["meta_positions"]["second"]
    
    for pos in reserved:
        if pos[0] == row and pos[1] == col:
            return True
    
    return False

def test_bit_list_to_raw_matrix():
    print('Testing bit_list_to_raw_matrix...', end='')
    # To make the test easier to read, bit_list contain distinct elements here
    # (in actual applications, bit_list would only have 0's and 1's)
    arg_bit_list = list(range(1, 72))
    arg_qr_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 9,
        'fixed_positions': {
            'ones': [
                [1, 3], [1, 4], 
            ],
            'zeros': [
                [2, 3], [2, 4],
            ]
        },
        'meta_positions': {
            'first': [
                [5, 2], [5, 3]
            ],
            'second': [
                [6, 2], [6, 3]
            ]
        }
        # key 'meta_patterns' skipped, since it is irrelevant for this task
    }

    expected = [
        [ 0, 50, 49, 48, 47, 20, 19, 18, 17],
        [ 0, 52, 51,  0,  0, 22, 21, 16, 15],
        [71, 54, 53,  0,  0, 24, 23, 14, 13],
        [70, 56, 55, 46, 45, 26, 25, 12, 11],
        [69, 58, 57, 44, 43, 28, 27, 10,  9],
        [68, 59,  0,  0, 42, 30, 29,  8,  7],
        [67, 60,  0,  0, 41, 32, 31,  6,  5],
        [66, 62, 61, 40, 39, 34, 33,  4,  3],
        [65, 64, 63, 38, 37, 36, 35,  2,  1]
    ]
    actual = bit_list_to_raw_matrix(arg_bit_list, arg_qr_layout)
    assert expected == actual
    print(' OK')

if __name__ == "__main__":
    test_bit_list_to_raw_matrix()


