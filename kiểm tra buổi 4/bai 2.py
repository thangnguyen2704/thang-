# bai2:Để kiểm tra xem một chuỗi cho trước có phải là palindrome hay không với thời gian chạy tuyến tính:
def is_palindrome_recursive(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    def is_palindrome_helper(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return is_palindrome_helper(left + 1, right - 1)
    return is_palindrome_helper(0, len(s) - 1)
# ví dụ
chuoi_can_kiem_tra = "A man, a plan, a canal, Panama!"
ket_qua = is_palindrome_recursive(chuoi_can_kiem_tra)
print(ket_qua)
