# Định nghĩa lớp Node để biểu diễn mỗi nút trong danh sách liên kết
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# Định nghĩa lớp LinkedList để quản lý danh sách liên kết
class LinkedList:
    def __init__(self):
        self.head = None  # Nút đầu tiên trong danh sách
        self.tail = None  # Nút cuối cùng trong danh sách
        self.length = 0    # Độ dài của danh sách

    def prepend(self, value):
        # Thêm một nút mới vào đầu danh sách
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        # Lấy và trả về nút đầu tiên khỏi danh sách
        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
# Tạo một đối tượng LinkedList mới
new_linked_list = LinkedList()
# Thêm các phần tử vào danh sách liên kết
new_linked_list.prepend(10)
new_linked_list.prepend(20)
new_linked_list.prepend(30)
# In danh sách liên kết trước khi pop
print("Danh sách liên kết trước khi pop:")
current_node = new_linked_list.head
while current_node:
    print(current_node.value, end=" ")
    current_node = current_node.next
# Pop phần tử đầu tiên
popped_node = new_linked_list.pop_first()
# In danh sách liên kết sau khi pop và phần tử đã pop
print("\nDanh sách liên kết sau khi pop:")
current_node = new_linked_list.head
while current_node:
    print(current_node.value, end=" ")
    current_node = current_node.next