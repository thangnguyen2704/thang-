numDays = int(input("How many day's temperature? "))#nhập vào số lượng ngày (numDays) mà họ muốn nhập nhiệt độ. Hàm int được sử dụng để chuyển đổi giá trị nhập vào thành một số nguyên.
total = 0#Biến total được khởi tạo với giá trị 0, sẽ được sử dụng để tính tổng các nhiệt độ.
temp = []#Biến temp là một danh sách rỗng, sẽ được sử dụng để lưu trữ nhiệt độ của mỗi ngày.
for i in range(numDays):#vòng lặp for được sử dụng để lặp qua từng ngày và yêu cầu người dùng nhập nhiệt độ cao nhất cho mỗi ngày.
  nextDay = int(input("Day" + str(i+1) + "'s high temp:"))# gán giá trị cho nextDay yêu cầu người dùng nhập nhiệt độ cao nhất cho một ngày cụ thể (được đại diện bởi biến )
  temp.append(nextDay)
  total += temp [i]#Nhiệt độ của mỗi ngày được thêm vào danh sách temp và cộng vào tổng total
avg = round(total/numDays, 2)#Sau khi lặp qua tất cả các ngày, biến avg được tính bằng cách chia tổng nhiệt độ (total) cho số ngày (numDays). Hàm round được sử dụng để làm tròn giá trị đến 2 chữ số thập phân.
print("\nAverage" + str(avg))#n ra màn hình giá trị trung bình của nhiệt độ cao nhất qua các ngày đã nhập.
above = 0# biến above được khởi tạo là giá trị 0
for i in temp:#Vòng lặp for tiếp theo được sử dụng để đếm số ngày có nhiệt độ cao hơn nhiệt độ trung bình (avg).
  if i > avg:  #Nếu nhiệt độ của một ngày (i) lớn hơn avg, thì biến above được tăng lên 1.
    above += 1
print(str(above)+" day(s) above average")# in ra màn hình số ngày có nhiệt độ cao hơn nhiệt độ trung bình.



