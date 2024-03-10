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
    def __str__(self):
        # Tạo chuỗi mô tả danh sách liên kết
        result = ''
        temp_node = self.head
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' > '
            temp_node = temp_node.next
        return result
# Tạo một đối tượng LinkedList mới
new_linked_list = LinkedList()
# Thêm các giá trị vào danh sách liên kết
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
# In ra mô tả của danh sách liên kết
print(new_linked_list)
