class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def NhomHang(self):
        groups = {}  # Dùng từ điển để lưu trữ nhóm các hàng giống nhau
        for i, row in enumerate(self.matrix):
            row_tuple = tuple(row)  # Chuyển hàng thành tuple để dùng làm khóa cho từ điển
            if row_tuple not in groups:
                groups[row_tuple] = [i]  # Nếu chưa có nhóm này, tạo mới và thêm chỉ mục hàng vào
            else:
                groups[row_tuple].append(i)  # Nếu đã có nhóm này, thêm chỉ mục hàng vào nhóm

        # In ra các nhóm hàng giống nhau
        for group in groups.values():
            print("Nhóm chỉ mục hàng:", group)

# Ma trận mẫu
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6]
]
# Tạo đối tượng Matrix và gọi phương thức NhomHang()
matrix_obj = Matrix(matrix_data)
matrix_obj.NhomHang()
