'''MatrixV = [
    ['#', '#', '#', 17 , 28, '#', '#'],
    ['#', '#', 27 , 0 ,  0 , 17 ,  17 ],
    ['#' , 11 , 0 , 0 ,  0 ,  0 ,  0  ],
    ['#'  , 0 , 0 ,14 ,  0 ,  0,   0  ],
    ['#' ,  0 , 0 , 0 ,  0 ,  0,   17 ],
    ['#',  '#', 0 , 0,   0 ,  0,   0 ],
    ['#',  '#', 0,  0,  '#',  0,   0]]

MatrixH = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', 16,   0 ,  0 , '#', '#'],
    ['#', 27,    0 , 0  , 0 ,  0 ,  0 ],
    [ 3,   0 ,   0 , 19,  0,   0,   0],
    [34,   0,    0,  0 ,  0 ,  0,  '#'],
    ['#', 30,    0 , 0,   0,   0,   0],
    ['#',  3,    0 , 0,  16,   0,   0]]
'''

'''MatrixV = [
    ['#', '#', '#', 16, 17, 16 , 25 , '#' , '#'],
    ['#', '#' , 16 , 0, 0 , 0 , 0 , '#' , '#'],
    ['#', 0, 0, 0, 0, 0, 13 , '#'],
    ['#', 0, 0, '#', 0, 0, 0 , '#'],
    ['#', '#', 10 , 7 , 0, 0, 0 , '#'],
    ['#', '#', 0, 0, 0, '#', 9 , 13],
    ['#', '#', 0, 0, 0 , 16 , 0 , 0],
    ['#', '#', '#' , 0, 0 , 0 , 0 , 0 , '#'],
    ['#', '#', '#', 0 , 0, 0, '#', '#'],
]

MatrixH = [
    ['#', '#', '#', '#', '#', '#', '#' , '#'],
    ['#', '#' , 15 , 0, 0, '#' , '#' , '#'],
    [24, 0, 0, 0, 0, 0, '#' , '#'],
    [15, 0, 0, 24, 0, 0, 0 , '#'],
    ['#', '#', '#' , 17 , 0, 0, 0 , '#'],
    ['#', 20, 0, 0, 0, '#', '#' , '#'],
    ['#', 8, 0, 0, 0 , 7 , 0 , 0],
    ['#', '#', 25 , 0, 0 , 0 , 0 , 0],
    ['#', '#', '#', 11, 0, 0, '#', '#'],
]
'''


MatrixV = [
    ['#', 16, 29 , 10, '#'],
    ['#', 0, 0, 0, '#'],
    ['#', 0 , 0 , 0 , 3],
    ['#', '#' , 0 , 0 , 0],
    ['#', '#', 0 , 0, 0]]
    
MatrixH = [
    ['#' , '#' , '#' , '#', '#'],
    [20, 0, 0, 0, '#'],
    [19, 0 , 0 , 0 , '#'],
    ['#', 10 , 0 , 0 , 0],
    ['#', 9, 0, 0, 0]]


'''MatrixV = [
    ['#', 23, 19 , 11],
    ['#', 0, 0, 0, ],
    ['#', 0 , 0 , 0 ],
    ['#', 0 , 0 , 0 ]]

MatrixH = [
      ['#', '#', '#' , '#'],
      [22 , 0, 0, 0, ],
      [21, 0 , 0 , 0 ],
      [10, 0 , 0 , 0 ]]

'''


# MatrixV and MatrixH are the input matrices that represent the vertical and horizontal clues
# '#' means a black cell, a positive number means a clue, and 0 means an empty cell

# rows and columns are the dimensions of the matrices
rows = len(MatrixV)
columns = len(MatrixH[0])

# variables is a list of tuples that represent the coordinates of the empty cells
variables = []

# column_constraint is a list of lists that represent the groups of empty cells in each column
column_constraint = []

# row_constraint is a list of lists that represent the groups of empty cells in each row
row_constraint = []

# column_sum is a list of numbers that represent the clues for each column group
column_sum = []

# row_sum is a list of numbers that represent the clues for each row group
row_sum = []

# for vertical matrix
# making column constraints and sums
for i in range(rows):
    for j in range(columns):
        if MatrixV[i][j] != '#':
            if MatrixV[i][j] == 0:
                variables.append((i, j))
            else:
                x, y = i, j
                cnt = 0
                group = []
                for k in range(i + 1, rows):
                    if MatrixV[k][j] != 0:
                        break
                    group.append((k, j))
                column_constraint.append(group)
                column_sum.append(MatrixV[x][y])

# for horizontal matrix
# making row constraints and sums
for i in range(rows):
    for j in range(columns):
        if MatrixH[i][j] != '#':
            if MatrixH[i][j] == 0:
                variables.append((i, j))
            else:
                x, y = i, j
                group = []
                for k in range(j + 1, columns):
                    if MatrixH[i][k] != 0:
                        break
                    group.append((i, k))
                row_constraint.append(group)
                row_sum.append(MatrixH[x][y])

# making domains for each variable
# each variable has domain {1, 2, 3, 4, 5, 6, 7, 8, 9}
domains = {}
for var in variables:
    domains[var] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# printing the results
print("Variables:", variables)
print("Row Constraint:", row_constraint)
print("Row Sum:", row_sum)
print("Column Constraint:", column_constraint)
print("Column Sum:", column_sum)
print("Domains:", domains)
