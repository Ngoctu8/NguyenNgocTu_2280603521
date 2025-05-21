def tao_tuple_tu_list(Lst):
    # Tạo tuple từ danh sách
    return tuple(Lst)
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách số. cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))
# Sử dụng hàm và in kết quả
my_tuple = tao_tuple_tu_list(numbers)
print("List:", numbers)
print("Tuple từ list:", my_tuple)





