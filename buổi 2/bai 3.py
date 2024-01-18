def foo(array):#Khởi tạo biến sum và product với giá trị khởi đầu là 0 và 1, tương ứng.
    sum = 0
    product = 1
    for i in array:# Vòng lặp for để tính tổng các phần tử trong mảng.
        sum += i
    for i in array: # Vòng lặp for để tính tích các phần tử trong mảng.
        product *= i
    print("Sum = "+str(sum )+",product ="+(product)) # In ra màn hình tổng và tích của các phần tử trong mảng.
 