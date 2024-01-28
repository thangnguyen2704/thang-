numDays = int(input("How many day's temperature?"))#(numDays) mà họ muốn nhập nhiệt độ. Hàm int được sử dụng để chuyển đổi giá trị nhập vào thành một số nguyên.
total = 0#Biến total được khởi tạo với giá trị 0, sẽ được sử dụng để tính tổng các nhiệt độ.
for i in range(1 ,numDays + 1):#òng lặp for được sử dụng để lặp qua mỗi ngày từ 1 đến numDays
    nextDay = int(input("Day " + str(i) + "s high temp:"))#Trong mỗi lần lặp, hàm input được sử dụng để yêu cầu người dùng nhập nhiệt độ cao nhất cho ngày đó (nextDay). Hàm int được sử dụng để chuyển đổi giá trị nhập vào thành một số nguyên.
    total += nextDay#Nhiệt độ của mỗi ngày được thêm vào biến total.
avg = round(total/numDays,2)#Sau khi lặp qua tất cả các ngày, biến avg được tính toán bằng cách chia tổng nhiệt độ (total) cho số ngày (numDays). Hàm round được sử dụng để làm tròn giá trị đến 2 chữ số thập phân.
print("\nAverage = " + str(avg))#in ra màn hình giá trị trung bình của nhiệt độ cao nhất qua các ngày đã nhập.