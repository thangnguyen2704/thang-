
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # Tạo một đối tượng Node mới với giá trị là value
        self.head = new_node
        self.tail = new_node
        self.length = 1
# Tạo một thể hiện mới của lớp LinkedList với giá trị ban đầu là 10
new_linked_list = LinkedList(10)
# In ra giá trị của node đầu tiên (head) trong danh sách liên kết
print(new_linked_list.head.value)
