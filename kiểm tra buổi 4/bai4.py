# bai 4 :kiểm tra hai từ( hoặc cụm từ) có đảo ngữ và so sánh có cùng bộ ký tự hay không?
def la_anagram(tu1, tu2):
    # Loại bỏ khoảng trắng và chuyển về chữ thường để so sánh không phân biệt chữ hoa chữ thường
    tu1 = tu1.replace(" ", "").lower()
    tu2 = tu2.replace(" ", "").lower()

    # Kiểm tra xem các ký tự được sắp xếp của cả hai từ có giống nhau không
    return sorted(tu1) == sorted(tu2)
# Sử dụng ví dụ
tu1 = "restful"
tu2 = "fluster"
ket_qua = la_anagram(tu1, tu2)

if ket_qua:
    print(f"{tu1} và {tu2} là anagram.")
else:
    print(f"{tu1} và {tu2} không phải là anagram.")
