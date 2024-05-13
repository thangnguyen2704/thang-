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
    def in_nguoc_de_qui(self, node):
        if node is None:
            return  # Nếu node là None, kết thúc đệ qui
        self.in_nguoc_de_qui(node.next)  # Gọi đệ qui cho node tiếp theo
        print(node.info, end=" ")  # In thông tin của node sau khi đệ qui quay lại
    def in_nguoc_khong_de_qui(self):
        stack = []  # Khởi tạo một stack để lưu trữ các node
        current = self.head
        while current:
            stack.append(current)  # Thêm node vào stack
            current = current.next
        while stack:
            node = stack.pop()  # Lấy node từ stack (ngược lại với thứ tự thêm vào)
            print(node.info, end=" ")  # In thông tin của node lấy ra từ stack
dslk = DanhSachLinkedList()
dslk.them_node(1)
dslk.them_node(2)
dslk.them_node(3)
dslk.them_node(4)
print("In ngược (đệ qui):")
dslk.in_nguoc_de_qui(dslk.head)  # In ngược sử dụng đệ qui từ head của danh sách
print("\nIn ngược (không đệ qui - sử dụng stack):")
dslk.in_nguoc_khong_de_qui()  # In ngược không sử dụng đệ qui, sử dụng stack
