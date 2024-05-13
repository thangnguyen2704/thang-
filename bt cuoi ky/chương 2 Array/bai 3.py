def is_duplicate_row(matrix):
    row_dict = {}  # từ điển để lưu trữ các hàng của ma trận
    for row in matrix:
        # Chuyển đổi list hàng thành tuple để có thể sử dụng làm key trong dictionary
        row_tuple = tuple(row)
        # Nếu hàng đã xuất hiện trong từ điển , có nghĩa là đã có hàng giống nhau
        if row_tuple in row_dict:
            return True
        # Thêm hàng vào từ điển với giá trị không quan trọng
        row_dict[row_tuple] = True
    # Nếu không tìm thấy hai hàng giống nhau, trả về False
    return False

# Khởi tạo ma trận ví dụ
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]  # Hàng này giống với hàng đầu tiên
]
# Kiểm tra và in kết quả
result = is_duplicate_row(matrix)
if result:
    print("Ma trận có ít nhất hai hàng giống nhau")
else:
    print("Ma trận không có hai hàng giống nhau")
