total = 0#Khởi tạo biến total với giá trị ban đầu là 0. Biến này sẽ được sử dụng để tính tổng của các số nhập vào.
count = 0#Khởi tạo biến count với giá trị ban đầu là 0. Biến này sẽ được sử dụng để đếm số lượng các số nhập vào.
while (True):#Bắt đầu một vòng lặp vô hạn (while True), có nghĩa là vòng lặp sẽ chạy mãi mãi cho đến khi có lệnh break được thực hiện.
    inp = input('enter a number: ')#Nhận đầu vào từ người dùng, yêu cầu nhập một số và lưu trữ giá trị nhập vào trong biến inp.
    if inp == 'done': break#Kiểm tra xem giá trị inp có phải là chuỗi "done" không. Nếu là "done", thoát khỏi vòng lặp bằng lệnh break.
    value = float(inp)#Chuyển đổi giá trị nhập vào từ dạng chuỗi sang số thực (float) và lưu vào biến value.
    total = total + value#Cộng giá trị mới (value) vào biến total để tính tổng.
    count = count + 1#Tăng giá trị của biến count lên 1 để đếm số lượng các số đã nhập vào.
    average = total/count#Tính giá trị trung bình (average) bằng cách chia tổng (total) cho số lượng (count).

print('Average :',average)#In ra màn hình giá trị trung bình của các số đã nhập vào. Đoạn mã này sẽ tiếp tục chờ đợi đầu vào từ người dùng cho đến khi họ nhập "done". Sau đó, nó sẽ tính và in ra giá trị trung bình của các số đã nhập.3