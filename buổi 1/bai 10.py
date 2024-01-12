# bai 10:How to convert a number from Decimal to Binary using recursion ?
def decimal_to_binary_recursive(n):
    # Base case: nếu n là 0 hoặc 1, trả về n
    if n == 0 or n == 1:
        return str(n)
    # Recursive case: chuyển đổi n // 2  và n % 2, sau đó ghép chuỗi
    else:
        return decimal_to_binary_recursive(n // 2) + str(n % 2) # n// 2 la chia lay phan nguyen + voi chuoi so n dã chia du

# Ví dụ sử dụng:
decimal_number = 30
binary_result = decimal_to_binary_recursive(decimal_number)
print(f"{decimal_number} ở hệ nhị phân là {binary_result}") # in ra chuoi nhi phan lay phan du  tu duoi len tren
