import os  # Import module os để tương tác với hệ thống tệp và thư mục

def add_word(dictionary):  # Định nghĩa hàm để thêm từ mới vào từ điển
    word = input("Nhập từ: ")  # Nhập từ từ người dùng
    meanings = []  # Khởi tạo danh sách để lưu các nghĩa của từ
    while True:  # Bắt đầu vòng lặp để nhập nhiều nghĩa cho từ
        meaning = input("Nhập nghĩa (để trống để dừng): ")  # Nhập nghĩa của từ từ người dùng
        if not meaning:  # Nếu không có nghĩa được nhập (rỗng) thì dừng vòng lặp
            break
        example = input("Nhập ví dụ: ")  # Nhập ví dụ cho nghĩa vừa nhập
        meanings.append((meaning, example))  # Thêm cặp (nghĩa, ví dụ) vào danh sách nghĩa
    dictionary[word] = meanings  # Thêm từ và các nghĩa của nó vào từ điển

def remove_word(dictionary):  # Định nghĩa hàm để xóa từ khỏi từ điển
    word = input("Nhập từ cần xóa: ")  # Nhập từ cần xóa từ người dùng
    if word in dictionary:  # Kiểm tra nếu từ tồn tại trong từ điển
        del dictionary[word]  # Xóa từ khỏi từ điển
        print(f"Từ '{word}' đã được xóa khỏi từ điển.")
    else:
        print(f"Từ '{word}' không tồn tại trong từ điển.")  # Thông báo nếu từ không tồn tại trong từ điển

def lookup_word(dictionary):  # Định nghĩa hàm để tra cứu nghĩa của từ
    word = input("Nhập từ cần tra cứu: ")  # Nhập từ cần tra cứu từ người dùng
    if word in dictionary:  # Kiểm tra nếu từ tồn tại trong từ điển
        meanings = dictionary[word]  # Lấy danh sách nghĩa của từ
        print(f"Những nghĩa của '{word}':")
        for i, (meaning, example) in enumerate(meanings, start=1):  # Duyệt và in ra các nghĩa và ví dụ
            print(f"{i}. {meaning}: {example}")
    else:
        print(f"Từ '{word}' không tồn tại trong từ điển.")  # Thông báo nếu từ không tồn tại trong từ điển


def write_dictionary_to_file(dictionary, file_path):
    with open(file_path, 'w', encoding='utf-8') as file: # mở file bằng tiếng việt
        for word, meanings_and_examples in dictionary.items():
            meanings, examples = zip(*meanings_and_examples)  # Tách nghĩa và ví dụ từ cặp
            meanings_str = ', '.join(meanings)  # Chuyển danh sách nghĩa thành chuỗi, các nghĩa cách nhau bởi ', '
            examples_str = ', '.join(examples)  # Chuyển danh sách ví dụ thành chuỗi, các ví dụ cách nhau bởi ', '
            file.write(f"{word}, {meanings_str}, {examples_str}\n")



def read_file_to_dictionary(file_path):
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(', ')
            if len(parts) >= 3:  # Đảm bảo có đủ từ, nghĩa và ví dụ
                word = parts[0]
                meanings = parts[1::2]  # Lấy các phần tử nghĩa từ dòng sau, mỗi phần tử cách nhau 2 bước
                examples = parts[2::2]  # Lấy các phần tử ví dụ từ dòng sau, mỗi phần tử cách nhau 2 bước
                meanings_and_examples = list(zip(meanings, examples))  # Kết hợp nghĩa và ví dụ thành cặp
                dictionary[word] = meanings_and_examples  # Lưu vào dictionary theo từ khóa
    return dictionary
def print_dictionary(dictionary):  # Định nghĩa hàm để in từ điển ra màn hình
    for word, meanings in sorted(dictionary.items()):  # Duyệt từng từ và nghĩa trong từ điển
        print(word)  # In từ ra màn hình
        for meaning, example in meanings:  # Duyệt các nghĩa và ví dụ của từ và in ra màn hình
            print(f"\t{meaning}: {example}")

def main():  # Định nghĩa hàm main để chạy chương trình
    student_id = "n21dcdt084"  # ID sinh viên
    filename = f"{student_id}_mang.txt"  # Tên tệp từ điển
    dictionary = read_file_to_dictionary(filename)  # Nạp từ điển từ tệp

    while True:  # Bắt đầu vòng lặp để hiển thị menu và thực hiện các chức năng
        print("\n1. Thêm từ mới")
        print("2. Xóa từ")
        print("3. Tra cứu nghĩa của từ")
        print("4. In từ điển")
        print("5. Lưu và thoát")
        choice = input("Chọn hành động: ")  # Chờ người dùng chọn hành động

        if choice == '1':
            add_word(dictionary)  # Gọi hàm để thêm từ mới
        elif choice == '2':
            remove_word(dictionary)  # Gọi hàm để xóa từ
        elif choice == '3':
            lookup_word(dictionary)  # Gọi hàm để tra cứu nghĩa của từ
        elif choice == '4':
            print_dictionary(dictionary)  # Gọi hàm để in từ điển ra màn hình
        elif choice == '5':
            write_dictionary_to_file(dictionary, filename)  # Gọi hàm để lưu từ điển và kết thúc chương trình
            print("Từ điển đã được lưu.")
            break  # Kết thúc vòng lặp và chương trình
        else:
            print("Lựa chọn không hợp lệ.")  # Thông báo nếu lựa chọn không hợp lệ

if __name__ == "__main__":  # Kiểm tra nếu chương trình được chạy trực tiếp từ Python
    main()  # Gọi hàm main để chạy chương trình
