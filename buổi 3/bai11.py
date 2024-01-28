prev_list =[1,2,3]#prev_list là danh sách ban đầu của bạn [1, 2, 3].
new_list = []#new_list là danh sách mới sẽ chứa các phần tử nhân 2 từ prev_list
for i in prev_list:#Vòng lặp for duyệt qua từng phần tử i trong prev_list.
    multiply_2 = i * 2#Mỗi phần tử i được nhân với 2 và kết quả được thêm vào new_list.
    new_list.append(multiply_2)#thêm giá trị của biến multiply_2 vào cuối danh sách new_list
    print(new_list)#in ra new_list