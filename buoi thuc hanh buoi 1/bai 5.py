def number(x, y):
    for n in range(x, y+1):
        s = sum_of_divisors(n)
        if s < n:
            print(n, "là deficient")
        elif s == n:
            print(n, "là perfect")
        else:
            print(n, "là abundant")
# Phương thức để tính tổng các ước số của n
def sum_of_divisors(n):
    if n == 1:
        return 1
    divisor_sum = 1  # 1 là ước số của mọi số nguyên dương
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Kiểm tra nếu i không phải là ước số kép
                divisor_sum += n // i
    return divisor_sum
# Nhập hai số nguyên dương x và y từ người dùng
x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y (y >= x): "))
# Kiểm tra và in ra phân loại của các số từ x đến y
print("Phân loại các số từ", x, "đến", y, ":")
number(x, y)
