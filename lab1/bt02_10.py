def dao_nguoc_chuoi(chuoi):
    # Đảo ngược chuỗi
    return chuoi[::-1]
#Sử dụng hàm và in kết quá
input_string = input("Nhập một chuỗi cần đảo ngược: ")
print("Chuỗi đã đảo ngược là:", dao_nguoc_chuoi(input_string))
