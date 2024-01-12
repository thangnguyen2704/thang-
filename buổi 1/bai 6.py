# bai 6  Fibonacci
def fibonacci(n):# nhap mot ham fibonacci co gia tri la n
    # assert n >=0 and int(n) == n , so fibonacci khong duoc la so am va phai la so nguyen
     if n in [0,1]: # n co gia tri bang 0 hoac 1
        return n # tra ve gia tri cua n
     else:
        return fibonacci(n-1) + fibonacci(n-2) # tra ve gia tri la so  fibonacci - 1 + so fibonacci - 2
a = fibonacci(4) # gan gia tri a bang so fibonacci co gia tri bang 4
print(a) # in ra a