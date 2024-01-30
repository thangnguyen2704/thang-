#bai 1 :đảo ngược 1 chuỗi tuyeens tính
def reverse_array_in_place(array):
    for i in range(len(array) // 2):
        array[i], array[-i - 1] = array[-i - 1], array[i]

    return array


array = [1, 2, 3, 4, 5]
print(reverse_array_in_place(array))
