# Hàm kiểm tra xem một ký tự có phải là toán tử hay không
def is_operator(char):
    return char in ['+', '-', '*', '/']
# Hàm xác định độ ưu tiên của các toán tử
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
# Phương thức chuyển đổi biểu thức từ dạng trung tố sang hậu tố
def HauTo(bt):
    output = []  # Chuỗi biểu diễn biểu thức hậu tố
    stack_operators = []  # Chồng lưu trữ các toán tử
    # Duyệt qua từng ký tự trong biểu thức trung tố
    for char in bt:
        # Bỏ qua khoảng trắng trong biểu thức
        if char == ' ':
            continue
        # Nếu là số, thêm vào chuỗi biểu thức hậu tố
        elif char.isdigit():
            output.append(char)
        # Nếu là toán tử
        elif is_operator(char):
            # Xử lý các toán tử trong biểu thức
            while (len(stack_operators) != 0 and
                   is_operator(stack_operators[-1]) and
                   precedence(stack_operators[-1]) >= precedence(char)):
                output.append(stack_operators.pop())
            stack_operators.append(char)
        # Nếu là dấu mở ngoặc
        elif char == '(':
            stack_operators.append(char)
        # Nếu là dấu đóng ngoặc
        elif char == ')':
            # Pop các toán tử từ stack và thêm vào output cho đến khi gặp dấu mở ngoặc
            while len(stack_operators) != 0 and stack_operators[-1] != '(':
                output.append(stack_operators.pop())
            # Loại bỏ dấu mở ngoặc khỏi stack
            stack_operators.pop()
    # Đẩy toàn bộ các toán tử còn lại trong stack vào output
    while len(stack_operators) != 0:
        output.append(stack_operators.pop())
    # Trả về biểu thức hậu tố dưới dạng chuỗi
    return ' '.join(output)
# Test phương thức HauTo
bt = '2 + 3 * 5'
print(HauTo(bt))  # Output: '2 3 5 * +'
