#13. Lấy thông tin bộ đệm mảng thông qua phương thức buffer_info()
from array import array
arr = array('i', [1, 2, 3, 4, 5])# Tạo một mảng với kiểu dữ liệu 'i' (integer)
buffer_info = arr.buffer_info()# lấy thông tin bộ đệm
print("Địa chỉ bộ đệm:", buffer_info[0])# In thông tin bộ đệm
print("Số lượng phần tử:", buffer_info[1])
