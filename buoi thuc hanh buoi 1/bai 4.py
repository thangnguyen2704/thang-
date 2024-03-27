def pascal(n):
    for line in range(0, n):
        # In ra số 1 ở đầu mỗi dòng
        print("n=" + str(line), 1, end=" ")
        # Tính toán và in ra các số ở giữa
        for i in range(1, line):
            print(calculate_binomial_coefficient(line, i), end=" ")
        # In ra số 1 ở cuối mỗi dòng
        if line > 0:
            print(1, end="")

        print()  # Xuống dòng
# Phương thức để tính hệ số nhị thức
def calculate_binomial_coefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res
# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập vào số nguyên dương n: "))
# In ra tam giác Pascal cho bậc n
pascal(n)
