def get_number(number):
  if number:
    return number#Nếu điều kiện đúng, hàm trả về giá trị của number.

  else:
    return "negative number"#nếu number là 0 hoặc False, hàm trả về chuỗi "negative number".

prev_list = [-1, 10, -20, 2, -90, 60, 45,20]#prev_list là danh sách ban đầu chứa các số nguyên.
new_list = [get_number(number) for number in prev_list]#Biểu thức danh sách này sử dụng vòng lặp for để duyệt qua từng phần tử number trong prev_list.
#Mỗi phần tử number được truyền vào hàm get_number(number)
print(new_list)
