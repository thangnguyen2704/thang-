#12. Chuyển đổi mảng thành chuỗi bằng phương thức tostring()
from array import array
arr = array('i', [1, 2, 3, 4, 5])# Tạo một mảng với kiểu dữ liệu 'i' (integer)
chuoi = arr.tobytes()# Chuyển đổi mảng thành chuỗi bằng phương thức tostring()
print(chuoi)# In chuỗi kết quả
