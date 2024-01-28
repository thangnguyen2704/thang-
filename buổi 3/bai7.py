myList = ['a', 'b', 'c', 'd', 'e', 'f']

# Sử dụng pop để loại bỏ phần tử tại vị trí có chỉ số là 2
myList.pop(2)

# Sử dụng del để loại bỏ các phần tử từ vị trí có chỉ số là 2 đến vị trí có chỉ số là 3 (không bao gồm vị trí có chỉ số là 4)
del myList[2:4]

# Sử dụng remove để loại bỏ phần tử có giá trị 'e'
#myList.remove('e')

# In ra danh sách myList sau khi loại bỏ các phần tử
print(myList)
