def neper(n):
    e_approx = 0  # Khởi tạo giá trị của e
    term = 1      # Số hạng đầu tiên của chuỗi
    for k in range(n + 1):
        e_approx += term  # Thêm số hạng hiện tại vào tổng
        term /= (k + 1)   # Tính số hạng tiếp theo

    return e_approx
# Nhập số nguyên n từ người dùng
n = int(input("Nhập vào số nguyên n (n ≥ 0): "))
# Tính và in ra tổng của a0 + a1 + ... + an
print("Tổng của a0 + a1 + ... + an là:", neper(n))
