def is_upper_triangle(matrix):
    n = len(matrix)  # Lấy số hàng của ma trận
    # Kiểm tra tính vuông của ma trận
    for i in range(n):
        if len(matrix[i]) != n:  # Nếu số cột của hàng i không bằng số hàng, không phải ma trận vuông
            return False
    # Kiểm tra tính tam giác trên của ma trận
    for i in range(n):
        for j in range(i + 1, n):  # Chỉ duyệt các phần tử phía trên đường chéo chính
            if matrix[i][j] != 0:  # Nếu có phần tử khác không phía trên đường chéo chính, không phải tam giác trên
                return False
    return True  # Nếu qua được tất cả các kiểm tra, ma trận là tam giác trên, trả về True
