# viết bằng phương thức không đệ qui
def fibonacci(n):
    fib_sequence = []
    if n == 0:
        return fib_sequence
    elif n == 1:
        fib_sequence.append(0)
        return fib_sequence
    else:
        fib_sequence.extend([0, 1])
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Nhập số nguyên n từ người dùng
n = int(input("Nhập vào số nguyên n >= 0: "))

# In ra dãy Fibonacci bậc 1 cho đến số thứ n
print("Dãy Fibonacci bậc 1 cho đến số thứ", n, "là:")
print(fibonacci(n))

