class CongArray:
    def Cong(a, b):
        result = [0] * max(len(a), len(b))  # Khởi tạo mảng kết quả có độ dài lớn nhất của a và b
        carry = 0  # Biến nhớ nếu có trường hợp tràn
        # Duyệt từ phải sang trái để thực hiện phép cộng từng cặp số
        for i in range(1, min(len(a), len(b)) + 1):
            total = a[-i] + b[-i] + carry  # Tổng của từng cặp số và biến nhớ
            result[-i] = total % 10  # Lưu chữ số hàng đơn vị vào kết quả
            carry = total // 10  # Cập nhật biến nhớ
        # Xử lý phần còn lại của mảng a hoặc b (nếu có)
        if len(a) > len(b):
            for i in range(len(a) - len(b) - 1, -1, -1):
                total = a[i] + carry
                result[i] = total % 10
                carry = total // 10
        elif len(b) > len(a):
            for i in range(len(b) - len(a) - 1, -1, -1):
                total = b[i] + carry
                result[i] = total % 10
                carry = total // 10
        # Kiểm tra xem kết quả có tràn số không
        if carry > 0:
            return [-1] * (len(result) + 1)  # Trả về mảng [-1, -1, ..., -1] nếu tràn số
        else:
            return result  # Trả về kết quả phép cộng
# Mảng mẫu
a = [1, 2, 3, 4]
b = [9, 9, 9]
# Thực hiện phép cộng và in kết quả
result = CongArray.Cong(a, b)
print("Kết quả:", result)
