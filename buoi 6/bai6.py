class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False
# Tạo một đối tượng LinkedList mới và thêm các phần tử vào danh sách liên kết
new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.append(20)
new_linked_list.append(30)
# In danh sách liên kết và kết quả tìm kiếm
print("Danh sách liên kết:", end=" ")
current_node = new_linked_list.head
while current_node:
    print(current_node.value, end=" ")
    current_node = current_node.next
target_value = 30
result = new_linked_list.search(target_value)
print("\nTìm kiếm giá trị", target_value, ":", result)
