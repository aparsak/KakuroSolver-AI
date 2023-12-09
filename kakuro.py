'''MatrixV = [
    ['#', '#', '#', 17, 28, '#', '#'],
    ['#', '#', 27, 0, 0, 17, 17],
    ['#', 11, 0, 0, 0, 0, 0],
    ['#', 0, 0, 14, 0, 0, 0],
    ['#', 0, 0, 0, 0, 0, 17],
    ['#', '#', 0, 0, 0, 0, 0],
    ['#', '#', 0, 0, '#', 0, 0]]

MatrixH = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', 16, 0, 0, '#', '#'],
    ['#', 27, 0, 0, 0, 0, 0],
    [3, 0, 0, 19, 0, 0, 0],
    [34, 0, 0, 0, 0, 0, '#'],
    ['#', 30, 0, 0, 0, 0, 0],
    ['#', 3, 0, 0, 16, 0, 0]]
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


'''MatrixV = [
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
'''

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

MatrixV = [
    ['#', '#', 14 , 29, '#'],
    ['#', 16, 0, 0, 7],
    ['#', 0 , 0 , 0 , 0],
    ['#', 0 , 0 , 0 , 0],
    ['#', '#', 0 , 0, '#']]

MatrixH = [
    ['#' , '#' , '#' , '#', '#'],
    ['#', 8, 0, 0, '#'],
    [15, 0 , 0 , 0 , 0],
    [30, 10 , 0 , 0 , 0],
    ['#', 13, 0, 0, '#']]

rows = len(MatrixV)
columns = len(MatrixH[0])

variables = []

# for vertical matrix
# making column constraints
neighbors = {}
for i in range(rows):
    for j in range(columns):
        if MatrixV[i][j] != '#':
            if MatrixV[i][j] == 0:
                variables.append((i, j))
            else:
                x, y = i, j
                cnt = 0
                for k in range(i + 1, rows):
                    if MatrixV[k][j] != 0:
                        break
                    if (i, j) not in neighbors:
                        neighbors[(i, j)] = list()
                    neighbors[(x, y)].append((k, j))

column_constraint = list(neighbors.values())  # Assign the value to column_constraint

# for Horizontal matrix
# making row constraints
neighbors = {}
for i in range(rows):
    for j in range(columns):
        if MatrixH[i][j] != '#':
            if MatrixH[i][j] == 0:
                variables.append((i, j))
            else:
                x, y = i, j
                for k in range(j + 1, columns):
                    if MatrixH[i][k] != 0:
                        break
                    if (i, j) not in neighbors:
                        neighbors[(i, j)] = list()
                    neighbors[(x, y)].append((i, k))

row_constraint = list(neighbors.values())

# calculating row_sum
values = []
for ele in neighbors:
    values.append(int(MatrixH[ele[0]][ele[1]]))
row_sum = values

# calculating column_sum
column_sum = [int(MatrixV[i][j]) for i in range(rows) for j in range(columns) if MatrixV[i][j] != '#' and MatrixV[i][j] != 0]

'''print("Variables:", variables)
print("Row Constraint:", row_constraint)
print("Row Sum:", row_sum)
print("Column Constraint:", column_constraint)
print("Column Sum:", column_sum)
'''