def is_symmetric(matrix):# dung de kiem tra tinh doi xung cua ma tran
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols :
        return False

    for i in range (rows):
        for j in range (cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
# khoi tao 1 ma tran bat ky
matrix = [
    [2,3,5],
    [5,8,6],
    [1,2,9]
]
result = is_symmetric(matrix)
if result:
    print("ma tran doi xung ")
else:
    print("ma tran khong doi xung ")
