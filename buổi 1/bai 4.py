# bai 4 : powerOfTwo(n)
def powerOfTwo(n):# bat dau ham tu powerOfTwo gia tri
     if n == 0:# neu n bang 0
       return 1 # tra gia tri powerOfTwo 1
     else:
       power = powerOfTwo(n-1) #gan power bang gia tri powerOfTwo giam di 1 don vi
       return power * 2 # tra ve gia tri power mu hai
a=powerOfTwo(4) # gia tri n bang 4
print(a) # in ra gia tri a bat dau tu powerOfTwo(4) goi powerOfTwo(3)....powerOfTwo(0) va tra ve 1
