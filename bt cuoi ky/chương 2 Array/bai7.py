def Nhan(a, b):
    # Chuyển đổi chuỗi số thành danh sách số nguyên
    num1 = [int(i) for i in str(a)]
    num2 = [int(i) for i in str(b)]

    # Khởi tạo mảng kết quả với tất cả các phần tử là -1
    result = [-1] * (len(num1) + len(num2))

    # Tính tích của a và b
    for i in range(len(num1)):
        for j in range(len(num2)):
            mul = num1[i] * num2[j]
            # Kiểm tra xem kết quả có tràn không
            if result[i + j] == -1:
                result[i + j] = mul
            else:
                result[i + j] += mul

    # Xử lý các tràn số
    carry = 0
    for i in range(len(result)):#
        if result[i] != -1:
            result[i] += carry
            carry = result[i] // 10
            result[i] %= 10

    # Kiểm tra xem kết quả có tràn không
    if carry != 0:
        return [-1] * (len(num1) + len(num2))
    else:
        # Chuyển đổi kết quả thành số nguyên
        res_str = ''.join(map(str, result[::-1])).lstrip('0')
        return int(res_str) if res_str else 0

# Sử dụng phương thức
a = 123
b = 456
print(Nhan(a, b))  # Output: 56088
