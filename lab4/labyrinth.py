### Skisse
# [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

# 90 grader med klokken:
# [
#  [7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]
# ]

# 90 grader mot klokken:
# [
#  [3, 6, 9],
#  [2, 5, 8],
#  [1, 4, 7]
# ]

### Skisse 2
# [
#  ['a', 'b'],
#  ['c', 'd'],
#  ['e', 'f'],
#  ['g', 'h'],
#  ['i', 'j']
# ],

# 90 grader med klokken
# [
#  ['i', 'g', 'e', 'c', 'a'],
#  ['j', 'h', 'f', 'd', 'b']
# ]


def rotate(grid, clockwise):
    new_grid = [[None] * len(grid) for _ in range(len(grid[0]))]
    # print(new_grid)
    
    if clockwise:
        # Med klokken
        for i in range(len(grid)):
            for j in range(len(grid[i]) - 1, -1, -1):
                new_grid[j][len(grid) - 1 - i] = grid[i][j]
    
    
    else:
        # Mot klokken
        for i in range(len(grid)- 1, -1,-1):
            for j in range(len(grid[i]) - 1, -1, -1):
                new_grid[len(grid[0]) - 1 - j][i] = grid[i][j]
    
    # print(new_grid)
    return new_grid

if __name__ == '__main__':
    import labyrinth_test
    labyrinth_test.run_all()
    """
    my_list = [
        ['a', 'b'],
        ['c', 'd'],
        ['e', 'f'],
        ['g', 'h'],
        ['i', 'j']
    ]
    

    my_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    """
    #rotate(my_list, False)
