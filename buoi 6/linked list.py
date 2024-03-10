class _Node:  # tạo Node
    __slots__ = '_element','_next'  # Node chứa 2 thuộc tính _element và _next

    def __init__(self,element,next):  # phương thức khởi tạo cửa lớp _Node chứa 2 tham số là element và next trỏ tới giá trị tiếp theo
        self._element = element    # gán giá trị của  tham số element cho thuộc tính _element
        self._next = next          # gán giá trị của  tham số next cho thuộc tính _next

class LinkedList:      # tạo class LinkedList
    def __init__(self): # phương thức khởi tạo của lớp LinkedList
        self._head = None # gán giá trị đầu là Null
        self._tail = None # tạo một biến tail để tham chiều của nút cuối cùng
        self._size = 0  # tạo một biến size để đếm số phần tử của danh sách liên kết

    def __len__(self):  # hàm len để kiểm tra số phần tử của danh sách liên kết
        return self._size  # trả về độ dài số phần tử của danh sách liên kết

    def isempty(self):  # hàm kiểm tra danh sách liên kết có rỗng không
        return  self._size == 0   # trả vê giá trị True nếu danh sách rỗng hoặc False nếu có phần tử

    def addlast(self,e): # hàm thêm phần tử e được chèn vào danh sách liên kêt
        newest = _Node(e,None) # tạo biến newest mang giá trị là e và trỏ tới Null
        if self.isempty():  # kiểm tra nếu danh sách rỗng
            self._head = newest #  gán giá trị đầu tiên của danh sách là newest
        else: # nếu không rỗng thì
            self._tail._next = newest # nếu không rỗng thì nút cuối cùng hiện tại trong danh sách sẽ trỏ tới nút mới tạo là newest
        self._tail = newest # gán giá trị cuối cùng của danh sách là newest
        self._size +=1 #tăng giá trị của size lên 1 để đếm số phần tử của danh sách liên kết

    def addfirst(self,e):  # tạo hàm chèn phần tử đầu vào danh sách liên kết
        newest = _Node(e,None) # tạo biên newest chưa giá trị là e và trỏ tới Null
        if self.isempty():  # nếu danh sách liên kết đang rỗng thì
            self._head=newest  # phần tử đầu của danh sách liên kết gán với biến cần chèn vào
            self._tail=newest  #  vì danh sách này mới có 1 phần tử nên phần tử nên phần tử cuối cũng là biến cần chèn vào
        else: # nếu danh sách không rỗng thì
            newest._next= self._head  # Nút newest sẽ trỏ đến phần tử đầu tiên của danh sách liên kết hiện tại, nút đầu tiên sẽ thành nút kế tiếp cần chèn vào
            self._head=newest # trỏ head đến phần tử cần chèn vào, nên phần tử đầu hiện tại sẽ là phần tử vừa thêm vào
        self._size += 1 # tăng kích thước của danh sách liên kết lên 1

    def addany(self,e,position): # tạo hàm chèn phần tử e vào vị trí position
        newest = _Node(e,None) # biến newest chứa giá trị e và trỏ tới Null
        p=self._head # gán p là phần tử đầu tiên của danh sách liên kết
        i=1 # gán i = 1
        while i<position-1: # kiểm tra vị trí của i có phải là vị trí cần chèn vào chưa
            p=p._next # trỏ tới phần tử kế tiếp trong danh sách liên kết
            i=i+1 # tăng biến đếm i
        newest._next=p._next # trỏ giá trị của biến cần chèn vào đến phần tử danh sách liên kết kế tiếp
        p._next= newest # trỏ giá trị tiếp theo của p là biến cần chèn vào
        self._size+=1 # tăng kích thước của danh sách liên kết


    def removefirst(self):  # tạo hàm xóa phần tử đầu tiên của danh sách liên kết
        if self.isempty():   # kiểm tra nếu danh sách trống
            print("List is empty") #nếu danh sách trống thì in ra list trống
            return
        e= self._head._element # gán e là giá trị của phần tử đầu tiên danh sách liên kết
        self._head=self._head._next # chúng ta sẽ trỏ head đến phần tử thứ 2, coi như phần tử thứ 2 là phần tử đầu, bỏ qua phần tử đầu tiên
        self._size-=1 # sau khi xóa thì giảm kích thước danh sách liên kết đi 1
        if self.isempty(): # kiểm tra lại nếu sau khi xóa danh sách liên kết trống
            self._tail=None # nếu linkedlist trống thì gán phần tử cuối cùng là None
        return e # trả về giá trị e để in ra giá trị của phần tử đã xóa nêu cần

    def removelast(self): # hàm xóa phần tử cuối cùng
        if self.isempty(): # kiểm tra nếu danh sách trống
            print("list is empty")#nếu danh sách trống thì in ra list trống
            return
        p=self._head # gán p là phần tử đầu tiên của danh sách liên kết
        i=1 # gán i =1
        while i< len(self)-1: # duyệt đến phần tử kế cuối
            p=p._next # duyệt tới phần tử kế tiếp
            i=i+1 # tăng biên i
        self._tail= p  # gán giá trị của cùng của danh sách liên kết là p( tức đang là giá trị kế cuối)
        p=p._next # duyết tới phần tử bị xóa để lấy giá trị của nó
        e=p._element # biến e lưu trữ giá trị phần tử bị xóa
        self._tail._next= None #  trỏ phần tử cuối cùng hiện tại( sau khi xóa phần tử cuối cùng ) là Null
        self._size-=1 # giảm kích thước của danh sách liên kết
        return e # trả về giá trị bị xóa

    def removeany(self, position):  # tạo hàm xóa tại vị trí position
        p=self._head  # p là phần tử đầu tiên
        i=1 #i=1
        while i<position-1: # vòng lặp chạy kiểm tra đến kế giá trị cần xóa chưa
            p=p._next # trỏ đến phần tử kế tiếp
            i=i+1 # tăng giá trị của i
        e=p._next._element # e gán = giá trị của của phần tử cần xóa
        p._next=p._next._next # trỏ giá trí tới nút hiện tại không trỏ tới giá trị cần xóa nữa mà trỏ tới phần tử tiếp theo của phần tử cần xóa
        self._size-=1 # giảm kích thước danh sách liên kết
        return  e # trả về giá trị cần xóa



    def search(self,key): # tạo hàm search để tìm kiếm giá trị key trong danh sách liên kết đơn
        p=self._head  # gán giá trị đầu là p
        index=0 # biến index để lưu số thứ tự của phần tử cần tìm
        while p: # tạo vòng lặp while
            if p._element == key: # nếu giá trị của phần tử hiện tại = key cần tìm thì trả về index là stt của phần tử đó
                return index # trả về giá trị index
            p=p._next # duyệt tới phần tử kế tiếp
            index += 1 # tăng index
        return -1 # nếu trong danh sách liên kết đó không có phần tử key cần tìm thì trả về giá trị là -1


    def display(self): # hàm để hiện ra phần tử được chèn vào
        p = self._head # gán p là giá trị đầu của danh sách liên kết
        while p: # sử dụng vòng lặp
            print(p._element,end='-->') # in ra giá trị của p
            p = p._next # trỏ p tới phần tử kế tiếp
        print()

L = LinkedList() # khởi tạo danh sách liên kết L
L.addlast(7) # thêm phần tử 7 vào danh sách liên kết
L.addlast(4) # thêm phần tử 4 vào danh sách liên kết
L.addlast(12) # thêm phần tử 12 vào danh sách liên kết
L.display() # in ra màn hình các phần tử của danh sách liên kết
print('Size:',len(L)) # in ra độ dài của danh sách liên kết
L.addlast(8) # thêm phần tử 8 vào danh sách liên kết
L.addlast(3) # thêm phần tử 3 vào danh sách liên kết
L.display()# in ra màn hình các phần tử của danh sách liên kết
print('Size:',len(L)) # in ra độ dài của danh sách liên kết
i=L.search(8)
# print(i)

L.addfirst(15) # chèn 15 vào đầu danh sách liên kết
L.display()
print('Size:',len(L)) # in ra độ dài của danh sách liên kết
L.addany(20,3) # chèn 20 vào vị trí thứ 3 của danh sách liên kết
L.display()
print('Size:',len(L)) # in ra độ dài của danh sách liên kết

ele = L.removefirst()
L.display()
print("element remove:",ele)

elelast=L.removelast()
L.display()
print("element remove ",elelast)

eleany=L.removeany(3)
L.display()
print("element remove ",eleany)
