newTuple = ('a','b','c','d','e')# Định nghĩa một tuple mới chứa các ký tự 'a', 'b', 'c', 'd', 'e'
def seachTuple(p_tuple,element):# Hàm tìm kiếm phần tử trong tuple

    for i in range (0,len(p_tuple)):# Duyệt qua từng phần tử của tuple
        if p_tuple[i] ==  element:  # Nếu phần tử trùng khớp với phần tử cần tìm
            return f"the{element} is found at {i}index"   # Trả về thông báo vị trí của phần tử trong tuple
    return 'the element is not found'# Nếu không tìm thấy, trả về thông báo không tìm thấy
print(seachTuple(newTuple,'b'))
# Gọi hàm searchTuple với tuple newTuple và phần tử 'b'