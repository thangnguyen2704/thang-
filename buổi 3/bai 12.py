prev_list = [-1,10,-20,2,-90,60,45,20]#prev_list là danh sách ban đầu chứa các số nguyên.
new_list = [number for number in prev_list if number > 0]#Trong list comprehension này, mỗi phần tử number trong prev_list được kiểm tra có lớn hơn 0 không (if number > 0). Nếu điều kiện này đúng, phần tử đó sẽ được bao gồm trong danh sách mới.
print(new_list)# in ra màn hình danh sách new_list.