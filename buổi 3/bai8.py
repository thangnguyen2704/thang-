my_List = [10,20,30,40,50,60,70,80,90]#my_List là một danh sách chứa các số từ 10 đến 90.
target = 50#là giá trị mục tiêu bạn muốn kiểm tra xem nó có trong danh sách my_List hay không.
if target in my_List:#để kiểm tra xem giá trị của target có tồn tại trong danh sách my_List không.
    print(f"{target} is in the list")#Nếu target tồn tại trong danh sách, dòng này sẽ in ra thông báo cho biết giá trị target có trong danh sách.
else:
    print(f"{target}is not in the list")#Nếu target không tồn tại trong danh sách, dòng này sẽ in ra thông báo cho biết giá trị target không có trong danh sách.