class TruArray:
    def Tru(a, b):
        result = [0] * len(a)  # Khởi tạo mảng kết quả có cùng độ dài với mảng a
        borrow = 0  # Biến vay nếu cần mượn khi trừ
        # Duyệt từ phải sang trái để thực hiện phép trừ từng cặp số
        for i in range(1, len(b) + 1):
            diff = a[-i] - b[-i] - borrow  # Hiệu của từng cặp số và biến vay
            if diff < 0:  # Nếu kết quả âm, cần mượn 1
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result[-i] = diff  # Lưu kết quả vào mảng kết quả
        # Xử lý phần còn lại của mảng a (nếu có)
        for i in range(len(b), len(a)):
            diff = a[i] - borrow  # Hiệu của số còn lại và biến vay
            if diff < 0:  # Nếu kết quả âm, cần mượn 1
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result[i] = diff  # Lưu kết quả vào mảng kết quả
        # Loại bỏ các số 0 dư thừa ở đầu mảng kết quả
        while result[0] == 0 and len(result) > 1:
            result.pop(0)
        return result  # Trả về kết quả phép trừ
# Mảng mẫu
a = [5, 7, 8, 3]
b = [2, 4, 6]
# Thực hiện phép trừ và in kết quả
result = TruArray.Tru(a, b)
print("Kết quả:", result)
