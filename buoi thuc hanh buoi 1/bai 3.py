#bai 9:How to find GCD ( Greatest Common Divisor) of two numbers using recursion?
def gcd_recursive(a, b): # nhap ham gcd_recursive nhan vao hai tham so a va b
    if b == 0: # neu b bang 0
        return a # thi gia tri tra ve la a
    else:
        return gcd_recursive(b, a % b) # gia tri tra ve la b và a chia du cho b

# Ví dụ sử dụng:
num1 = 372# so thu nhat bang 48
num2 = 12# so thu hai bang 18
result = gcd_recursive(num1, num2)# tong bang gia tri uoc chung lon nhat la
print(f"GCD của {num1} và {num2} là {result}")# in ra uoc chung lon nhat cua so 1 va 2 la tong