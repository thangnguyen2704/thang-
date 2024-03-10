class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Khởi tạo thuộc tính next là None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # Tạo một đối tượng Node mới
        self.head = new_node
        self.tail = new_node
        self.length = 1
# Tạo một thể hiện mới của lớp LinkedList với giá trị ban đầu là 10
new_linked_list = LinkedList(10)
# In ra danh sách liên kết vừa được tạo
print(new_linked_list)
