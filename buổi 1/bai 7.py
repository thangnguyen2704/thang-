# bai 7 :How to find the sum of digits of a positive integer number using recursion
def sum_digits(n):
    if n > 0: # neu n lon hon 0
        return n +  sum_digits(n -1) # tra ve gia tri n + sum_digits(n -1) lan luot cho den khi nho hon 0 
    return 0 # neu < 0 thi ket thuc tra ve gia tri 0
n = int (input()) # gan n bang gia tri dau ra la kieu so nguyen
if n < 0 : # neu n nho hon 0
   print ("yeu cau nhap lai") # in ra yeu cau
else:
    print (sum_digits(n))# in ra tinh tong sum_digits(n)


