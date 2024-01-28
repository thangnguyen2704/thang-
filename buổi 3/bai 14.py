prev_list = [-1,10,-20,2,-90,60,45,20]#prev_list là danh sách ban đầu chứa các số nguyên.
new_list = [number if number > 0 else 0 for number in prev_list]#Nếu number đó lớn hơn 0, giữ nguyên giá trị, ngược lại, thay thế bằng 0.
print(new_list)# in ra màn hình danh sách new_list.