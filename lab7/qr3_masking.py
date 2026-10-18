import copy
from qr2_matrix_completion import * 

def should_flip(row, col, mask_no):
    if mask_no == 0 and (row + col) % 2 == 0:
         return True
    elif mask_no == 1 and row % 2 == 0:
         return True
    elif mask_no == 2 and col % 3 == 0:
         return True
    elif mask_no == 3 and (row + col) % 3 == 0:
         return True
    elif mask_no == 4 and (row//2 + col//3) % 2 == 0:
         return True
    elif mask_no == 5 and (row*col) % 2 + (row*col) % 3 == 0:
         return True
    elif mask_no == 6 and ((row*col) % 2 + (row*col) % 3) % 2 == 0:
         return True
    elif mask_no == 7 and ((row+col) % 2 + (row*col) % 3) % 2 == 0:
         return True
    else:
        return False

def get_masked_matrix(matrix, mask_no):
    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            if should_flip(i, j, mask_no):
                new_matrix[i].append(0 if matrix[i][j] == 1 else 1)
            else:
                new_matrix[i].append(matrix[i][j])
    
    return new_matrix

def score_matrix(matrix):
    zeros = 0
    ones = 0
    for i in matrix:
        for j in i:
            if j == 0:
                zeros += 1
            else:
                ones += 1

    return abs(zeros-ones)

def get_refined_matrix(raw_matrix, error_correction_level, qr_layout):
    score = 9999
    best_matrix = []
    best_mask = 8

    for i in range(0, 7): 
        matrix = copy.deepcopy(raw_matrix)
        matrix = get_masked_matrix(matrix, i)

        set_meta_fields(matrix, error_correction_level, i, qr_layout)
        set_fixed_fields(matrix, qr_layout)
    
        new_score = score_matrix(matrix) 
        if new_score < score and i < best_mask:
            score = new_score
            best_mask = i
            best_matrix = copy.deepcopy(matrix)

    return best_matrix

if __name__ == "__main__":
    test_get_masked_matrix()
    test_score_matrix()


