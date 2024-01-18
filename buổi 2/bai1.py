import array

my_array = array.array('i') # tạo một giá trị my_array có giá trị là array.array kiểu integer
print(my_array)#in ra my_array
my_array1 = array.array('i' ,[1,2,3,4])#tạo một my_array1 có phần tử là [1,2,3,4]
print(my_array1)#in ra my_array1

import numpy as np # sử dụng toàn bộ các chức năng của numpy ghi tắt là np
np_array = np.array([], dtype=int)# khởi tạo một np.array rỗng với kiểu dữ liểu là số nguyên
print(np_array)#in ra giá trị np_array
np_array1 = np.array([1,2,3,4])# tạo một np_array1 có phần tử là [1,2,3,4]
print(np_array1)#in ra giá trị np_array1