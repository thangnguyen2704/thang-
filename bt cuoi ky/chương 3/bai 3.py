class Node:
    def __init__(self, hs, sm, kt=None):
        self.HeSo = hs  # Hệ số của số hạng
        self.SoMu = sm  # Số mũ của số hạng
        self.KeTiep = kt  # Con trỏ đến số hạng kế tiếp
class DaThuc:
    def __init__(self):
        self.head = None  # Khởi tạo đa thức rỗng
    def Cong(self, dathuc2):
        p1 = self.head
        p2 = dathuc2.head
        result = DaThuc()  # Đa thức kết quả
        while p1 is not None and p2 is not None:
            hs_sum = p1.HeSo + p2.HeSo
            sm = p1.SoMu  # Số mũ không thay đổi sau khi cộng
            if hs_sum != 0:  # Chỉ thêm số hạng không bằng 0 vào kết quả
                result.ThemSoHang(hs_sum, sm)
            p1 = p1.KeTiep
            p2 = p2.KeTiep
        # Thêm các số hạng còn lại từ dathuc1 hoặc dathuc2 vào kết quả
        while p1 is not None:
            result.ThemSoHang(p1.HeSo, p1.SoMu)
            p1 = p1.KeTiep
        while p2 is not None:
            result.ThemSoHang(p2.HeSo, p2.SoMu)
            p2 = p2.KeTiep
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
