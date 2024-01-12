#bai 5.Giai thua
def factorial(n): # nhap mot ham factorial co gia tri la n giai thua
   if n in [0,1]: # neu gia tri n bang o giai thua hoac 1 giai thua
     return 1 # tra ve gia tri la bang 1
   else:
     return n * factorial(n-1) # tra ve ket qua n! = n * (n -1)!
a = factorial(5) # gan a bang nhap gia tri 5 !
print(a) # in ra ket qua