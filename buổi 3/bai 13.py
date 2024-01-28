sentence = 'My name is Elshad'#sentence là một chuỗi văn bản đơn giản chứa câu "My name is Elshad".

def is_consanant(letter):#is_consanant là một hàm kiểm tra xem một ký tự có phải là phụ âm hay không.
    vowels ='aeiou'
    return letter.isalpha() and letter.lower() not in vowels#letter.isalpha() kiểm tra xem letter có phải là một ký tự chữ cái hay không.
#letter.lower() not in vowels kiểm tra xem letter (chuyển đổi thành chữ thường) có nằm trong chuỗi nguyên âm vowels hay không.

consanant = [i for i in sentence if is_consanant(i)]#Biểu thức danh sách (list comprehension) này tạo ra danh sách consanant chứa các ký tự từ sentence mà không phải là nguyên âm, sử dụng hàm is_consanant để kiểm tra điều kiện.
#Vòng lặp duyệt qua từng ký tự i trong sentence.Nếu is_consanant(i) là True (tức là i là một phụ âm), thì i sẽ được bao gồm trong danh sách consanant.
print(consanant)#in ra consanant