def count_words(file_path):
    word_counts = {}

    # Mở tệp và đọc các từ
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()

    # Đếm số lần xuất hiện của từng từ
    for word in words:
        word = word.lower()  # Chuyển đổi từ thành chữ thường để loại bỏ sự phân biệt về chữ hoa/chữ thường
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts



# Kiểm tra hàm với các test case
file_path = 'P1_data.txt'
assert count_words(file_path)['success'] == 3

file_path = 'P1_data.txt'
print(count_words(file_path)['man'])
