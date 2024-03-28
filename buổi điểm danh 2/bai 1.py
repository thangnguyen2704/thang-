def max_in_sliding_window(num_list, size):
    if not num_list:
        return []
    result = []
    window = []  # List để lưu trữ các chỉ mục của các số trong cửa sổ
    # Duyệt qua từng số trong danh sách
    for i, num in enumerate(num_list):
        # Loại bỏ các chỉ mục khỏi cửa sổ vượt quá kích thước cửa sổ
        while window and window[0] <= i - size:
            window.pop(0)
        # Loại bỏ các phần tử nhỏ hơn phần tử mới thêm vào từ phía sau cửa sổ
        while window and num_list[window[-1]] < num:
            window.pop()
        # Thêm chỉ mục của phần tử vào cửa sổ
        window.append(i)

        # Nếu cửa sổ đã đủ kích thước, thêm số lớn nhất vào kết quả
        if i >= size - 1:
            result.append(num_list[window[0]])

    return result
# Kiểm tra với input đã cung cấp
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
size = 3
print(max_in_sliding_window(num_list, size))  # Output: [5, 5, 5, 5, 10, 12, 33, 33]
