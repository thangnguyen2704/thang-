shoppingList = ['MILK', 'CHEESE', 'BUTTER']

# Duyệt qua từng phần tử trong shoppingList và thêm dấu '+' vào cuối mỗi phần tử
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"

# In ra shoppingList sau khi thêm dấu '+'
print(shoppingList)

# Khởi tạo một danh sách rỗng
empty = []

# Duyệt qua từng phần tử trong danh sách rỗng (chú ý là không có phần tử nào để duyệt qua)
for i in empty:
    print("I am empty")

# Vì danh sách rỗng, dòng in trên sẽ không được thực hiện và không có gì sẽ được in ra màn hình
