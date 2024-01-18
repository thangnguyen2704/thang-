import array

# Tạo một mảng số nguyên có tên là my_array1 với các giá trị 1, 2, 3, 4, 5
my_array1 = array.array('i', [1, 2, 3, 4, 5])

# Định nghĩa một hàm thực hiện tìm kiếm tuyến tính
def linear_search(arr, target):
    # Duyệt qua các chỉ số của mảng
    for i in range(len(arr)):
        # Kiểm tra nếu phần tử hiện tại bằng giá trị cần tìm
        if arr[i] == target:
            # Nếu tìm thấy, trả về chỉ số
            return i
    # Nếu không tìm thấy giá trị cần, trả về -1
    return -1

# Gọi hàm linear_search với my_array1 và giá trị cần tìm là 8, sau đó in kết quả ra màn hình
print(linear_search(my_array1, 8))
