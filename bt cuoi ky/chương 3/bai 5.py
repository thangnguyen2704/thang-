class Node:
    def __init__(self, hs, sm, kt=None):
        self.HeSo = hs  # Hệ số của số hạng
        self.SoMu = sm  # Số mũ của số hạng
        self.KeTiep = kt  # Con trỏ đến số hạng kế tiếp

class DaThuc:
    def __init__(self):
        self.head = None  # Khởi tạo đa thức rỗng

    def Tich(self, dathuc2):
        p1 = self.head
        p2 = dathuc2.head
        result = DaThuc()  # Đa thức kết quả

        while p1 is not None:
            temp_p2 = p2  # Khởi tạo con trỏ mới của dathuc2 ở mỗi lần duyệt p1
            while temp_p2 is not None:
                hs_tich = p1.HeSo * temp_p2.HeSo
                sm_tong = p1.SoMu + temp_p2.SoMu
                result.ThemSoHang(hs_tich, sm_tong)
                temp_p2 = temp_p2.KeTiep
            p1 = p1.KeTiep

        result.RutGon()  # Rút gọn đa thức kết quả
        return result

    def ThemSoHang(self, hs, sm):
        new_node = Node(hs, sm)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.KeTiep is not None:
                last_node = last_node.KeTiep
            last_node.KeTiep = new_node

    def RutGon(self):
        prev = None
        current = self.head

        while current is not None:
            # Xoá số hạng có hệ số bằng 0
            if current.HeSo == 0:
                if prev is None:
                    self.head = current.KeTiep
                else:
                    prev.KeTiep = current.KeTiep
                current = current.KeTiep
                continue

            # Rút gọn các số hạng giống nhau (cùng số mũ)
            temp = current.KeTiep
            while temp is not None and temp.SoMu == current.SoMu:
                current.HeSo += temp.HeSo
                temp = temp.KeTiep

            prev = current
            current = current.KeTiep

    def InDaThuc(self):
        current = self.head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep
        print()

# Test
dathuc1 = DaThuc()
dathuc1.ThemSoHang(3, 2)
dathuc1.ThemSoHang(4, 1)

dathuc2 = DaThuc()
dathuc2.ThemSoHang(2, 1)
dathuc2.ThemSoHang(1, 0)

print("Da thuc 1:")
dathuc1.InDaThuc()

print("Da thuc 2:")
dathuc2.InDaThuc()

dathuc_tich = dathuc1.Tich(dathuc2)
print("Tich cua hai da thuc:")
dathuc_tich.InDaThuc()
