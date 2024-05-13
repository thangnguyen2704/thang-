class Node:
    def __init__(self, he_so, so_mu, ke_tiep=None):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = ke_tiep
class DanhSachDaThuc:
    def __init__(self):
        self.head = None
    def them_so_hang(self, he_so, so_mu):
        if self.head is None:
            self.head = Node(he_so, so_mu)
        else:
            current = self.head
            while current.ke_tiep:
                current = current.ke_tiep
            current.ke_tiep = Node(he_so, so_mu)
    def chep(self):
        da_thuc_copy = DanhSachDaThuc()
        current = self.head
        while current:
            da_thuc_copy.them_so_hang(current.he_so, current.so_mu)
            current = current.ke_tiep
        return da_thuc_copy

    def in_da_thuc(self):
        current = self.head
        while current:
            print(f"{current.he_so}x^{current.so_mu}", end=" ")
            current = current.ke_tiep
        print()
# Sử dụng
da_thuc = DanhSachDaThuc()
da_thuc.them_so_hang(3, 2)
da_thuc.them_so_hang(-1, 1)
da_thuc.them_so_hang(5, 0)
print("Đa thức gốc:")
da_thuc.in_da_thuc()
da_thuc_copy = da_thuc.chep()
print("Đa thức sao chép:")
da_thuc_copy.in_da_thuc()
