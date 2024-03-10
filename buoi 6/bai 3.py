class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        # Khởi tạo danh sách liên kết với một node đầu tiên (head) và node cuối cùng (tail)
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, value):
        # Tạo một node mới
        new_node = Node(value)
        # Nếu danh sách liên kết trống, gán cả head và tail cho node mới
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Ngược lại, thêm node mới vào cuối danh sách và cập nhật tail
            self.tail.next = new_node
            self.tail = new_node
        # Tăng độ dài của danh sách liên kết
        self.length += 1
# Tạo một đối tượng LinkedList mới
new_linked_list = LinkedList()
# Thêm các giá trị vào danh sách liên kết
new_linked_list.append(10)
new_linked_list.append(20)
# In ra độ dài của danh sách liên kết sau khi thêm các giá trị
print(new_linked_list.length)
