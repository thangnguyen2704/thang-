class Person:
    def __init__(self, name, age):
        # Khởi tạo đối tượng Person với tên và tuổi
        self.name = name
        self.age = age
    def __str__(self):
        # Trả về chuỗi mô tả đối tượng khi được chuyển đổi thành chuỗi
        return f"Person {self.name} - {self.age}"
# Tạo một đối tượng Person mới
new_person = Person("Elshad", 20)
# In ra mô tả của đối tượng Person
print(new_person)
