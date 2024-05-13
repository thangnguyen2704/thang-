class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso  # Hệ số của số hạng
        self.SoMu = somu  # Số mũ của số hạng
        self.KeTiep = None  # Con trỏ đến số hạng kế tiếp
# Hàm thêm một số hạng vào đa thức
def Them(dathuc, heso, somu):
    new_node = Node(heso, somu)
    # Nếu danh sách đa thức đang trống
    if dathuc is None:
        dathuc = new_node
    else:
        current = dathuc
        # Tìm vị trí để chèn số hạng mới theo thứ tự giảm dần của số mũ
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node
# Hàm in ra đa thức
def InDaThuc(dathuc):
    current = dathuc
    while current is not None:
        print(f"{current.HeSo}x^{current.SoMu}", end=" ")
        current = current.KeTiep
        if current is not None:
            print("+", end=" ")
    print()
# Phương thức rút gọn đa thức
def RutGon(dathuc):
    current = dathuc
    while current is not None and current.KeTiep is not None:
        next_node = current.KeTiep
        # Nếu hai số hạng có cùng số mũ, thực hiện phép rút gọn
        if current.SoMu == next_node.SoMu:
            current.HeSo += next_node.HeSo
            current.KeTiep = next_node.KeTiep
            del next_node
        else:
            current = current.KeTiep
    # Loại bỏ các số hạng có hệ số bằng 0
    current = dathuc
    prev_node = None
    while current is not None:
        if current.HeSo == 0:
            if prev_node is None:
                dathuc = current.KeTiep
            else:
                prev_node.KeTiep = current.KeTiep
            del current
        else:
            prev_node = current
            current = current.KeTiep
    return dathuc
if __name__ == "__main__":
    dathuc = None  # Khởi tạo đa thức rỗng
    # Thêm các số hạng vào đa thức
    Them(dathuc, 3.5, 2)
    Them(dathuc, -2.1, 1)
    Them(dathuc, 1.0, 0)
    Them(dathuc, -1.0, 0)
    # In ra đa thức trước khi rút gọn
    print("Da thuc truoc khi rut gon:")
    InDaThuc(dathuc)
    # Rút gọn đa thức
    dathuc = RutGon(dathuc)
    # In ra đa thức sau khi rút gọn
    print("Da thuc sau khi rut gon:")
    InDaThuc(dathuc)
