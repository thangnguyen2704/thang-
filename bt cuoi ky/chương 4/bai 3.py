def bt_GiaTri(bt):
  """
  Tính toán giá trị của biểu thức số học dạng trung tố.

  Args:
    bt: Chuỗi biểu diễn biểu thức số học.

  Returns:
    Giá trị số thực của biểu thức.
  """
  # Khởi tạo hai cái chồng rỗng
  toan_hang = []
  toan_tu = []

  # Duyệt qua từng ký tự trong chuỗi biểu thức
  for c in bt:
    if c.isdigit():
      # Thêm số vào chồng toán hạng
      toan_hang.append(int(c))
    elif c in "+-*/":
      # Xử lý toán tử
      while len(toan_tu) > 0 and uu_tien(toan_tu[-1]) >= uu_tien(c):
        toan_hang.append(tinh_toan(toan_tu.pop(), toan_hang.pop(), toan_hang.pop()))
      toan_tu.append(c)
  # Tính toán các toán tử còn lại
  while len(toan_tu) > 0:
    toan_hang.append(tinh_toan(toan_tu.pop(), toan_hang.pop(), toan_hang.pop()))

  # Lấy giá trị cuối cùng trong chồng toán hạng là kết quả
  return toan_hang[0]

def uu_tien(toan_tu):
  """
  Xác định thứ tự ưu tiên của toán tử.

  Args:
    toan_tu: Ký tự toán tử.

  Returns:
    Thứ tự ưu tiên (cao hơn thì được tính toán trước).
  """
  if toan_tu in "+-":
    return 1
  elif toan_tu in "*/":
    return 2
  else:
    return 0

def tinh_toan(toan_tu, toan_hang2, toan_hang1):
  """
  Tính toán giá trị dựa trên toán tử và hai toán hạng.

  Args:
    toan_tu: Ký tự toán tử.
    toan_hang1: Toán hạng thứ nhất.
    toan_hang2: Toán hạng thứ hai.

  Returns:
    Kết quả tính toán.
  """
  if toan_tu == "+":
    return toan_hang1 + toan_hang2
  elif toan_tu == "-":
    return toan_hang1 - toan_hang2
  elif toan_tu == "*":
    return toan_hang1 * toan_hang2
  else:
    return toan_hang1 / toan_hang2

bt='3+3*3'
print(bt_GiaTri(bt))