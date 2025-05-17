def dao_nguoc_list(lst):
    # Đảo ngược danh sách
    return lst[::-1]
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách số. cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))

# Sử dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách đã đảo ngược là:", list_dao_nguoc)

