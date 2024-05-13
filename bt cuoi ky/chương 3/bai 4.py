class Node:
    def __init__(self, hs, sm, kt=None):
        self.HeSo = hs  # Hệ số của số hạng
        self.SoMu = sm  # Số mũ của số hạng
        self.KeTiep = kt  # Con trỏ đến số hạng kế tiếp
class DaThuc:
    def __init__(self):
        self.head = None  # Khởi tạo đa thức rỗng
    def DoiDau(self):
        current = self.head
        while current is not None:
            current.HeSo = -current.HeSo  # Đổi dấu của hệ số
            current = current.KeTiep
    def ThemSoHang(self, hs, sm):
        new_node = Node(hs, sm)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.KeTiep is not None:
                last_node = last_node.KeTiep
            last_node.KeTiep = new_node
    def InDaThuc(self):
        current = self.head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep
        print()
dathuc = DaThuc()
dathuc.ThemSoHang(3, 2)
dathuc.ThemSoHang(-5, 1)
dathuc.ThemSoHang(2, 0)
print("Da thuc truoc khi doi dau:")
dathuc.InDaThuc()
dathuc.DoiDau()
print("Da thuc sau khi doi dau:")
dathuc.InDaThuc()
