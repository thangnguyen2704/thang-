# bai 3 : chuyển một số nguyên thành một chuỗi ,đảo ngược chuỗi và sau đó chuyển nó lại thành một số nguyên 
def dao_nguoc_so_nguyen(num):
    # Kiểm tra xem số có là số âm không
    is_negative = num < 0
    # chuyển giá trị tuyệt đối của số thành chuỗi, đảo ngược chuỗi bằng cách sử dụng cú pháp slicing ([::-1]),
    chuoi_dao_nguoc = str(abs(num))[::-1]
    # Chuyển chuỗi đảo ngược trở lại thành số nguyên
    so_nguyen_dao_nguoc = int(chuoi_dao_nguoc)
    # Trả về số nguyên đảo ngược với dấu gốc
    return -so_nguyen_dao_nguoc if is_negative else so_nguyen_dao_nguoc
# Ví dụ sử dụng
so_nguyen_nhap = 1234
so_nguyen_dao_nguoc = dao_nguoc_so_nguyen(so_nguyen_nhap)
print(so_nguyen_dao_nguoc)
