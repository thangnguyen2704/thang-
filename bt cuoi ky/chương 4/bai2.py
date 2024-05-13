class Node:
    def __init__(self, info):
        self.info = info  # Thông tin của node
        self.next = None  # Con trỏ next chỉ đến node tiếp theo (ban đầu là None)
class DanhSachLinkedList:
    def __init__(self):
        self.head = None  # Khởi tạo danh sách với head là None (danh sách rỗng)

    def them_node(self, info):
        new_node = Node(info)  # Tạo một node mới với thông tin là 'info'
        if self.head is None:
            self.head = new_node  # Nếu danh sách rỗng, node mới trở thành head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Thêm node mới vào cuối danh sách
    def dao_nguoc(self):
        prev = None  # Biến prev để lưu trữ node trước đó
        current = self.head  # Bắt đầu từ head của danh sách
        while current:
            next_node = current.next  # Lưu node tiếp theo trước khi thay đổi con trỏ next
            current.next = prev  # Đảo chiều con trỏ next của current node
            prev = current  # Cập nhật prev để di chuyển tiếp
            current = next_node  # Di chuyển đến node tiếp theo trong danh sách
        self.head = prev  # Cập nhật head mới sau khi đã đảo ngược
    def in_dslk(self):
        current = self.head
        while current:
            print(current.info, end=" ")  # In thông tin của node
            current = current.next  # Di chuyển đến node tiếp theo trong danh sách
        print()  # In xuống dòng để kết thúc dòng in
dslk = DanhSachLinkedList()
dslk.them_node(1)
dslk.them_node(2)
dslk.them_node(3)
dslk.them_node(4)
print("Danh sách trước khi đảo ngược:")
dslk.in_dslk()  # In danh sách trước khi đảo ngược
dslk.dao_nguoc()  # Đảo ngược danh sách
print("Danh sách sau khi đảo ngược:")
dslk.in_dslk()  # In danh sách sau khi đảo ngược
