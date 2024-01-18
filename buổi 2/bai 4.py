 from array import *
 arr1 = array('i',[1,2,3,4,5,6])# Khởi tạo mảng arr1 với kiểu dữ liệu 'i' (integer) và các phần tử là 1, 2, 3, 4, 5, 6.
 arr2 = array('d',[1.3,1.5,1.6])# Khởi tạo mảng arr2 với kiểu dữ liệu 'd' (double) và các phần tử là 1.3, 1.5, 1.6.

 def traversrearray(array):# Định nghĩa hàm traversrearray nhận một tham số là một mảng và in ra từng phần tử trong mảng đó.
     for i in array:
         print(i)
 traversrearray(arr1)# Gọi hàm traversrearray và truyền mảng arr1 làm đối số.