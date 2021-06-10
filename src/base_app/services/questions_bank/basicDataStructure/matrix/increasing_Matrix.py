def find_increasing_matrix_1(r,c):
    mat = [[0 for _ in range(c)] for _ in range(r)]
    count = 1
    for i in range(r):
        for j in range(c):
            mat[i][j] = count
            count += 1
    # print(mat)
    for item in mat:
        print(item)


def find_increasing_matrix_2(r,c):
    mat = [[0 for _ in range(c)] for _ in range(r)]
    count = 1
    for i in range(c):
        for j in range(r):
            mat[j][i] = count
            count += 1
    # print(mat)
    for item in mat:
        print(item)


r=4
c=5
find_increasing_matrix_1(r, c)
find_increasing_matrix_2(r, c)
