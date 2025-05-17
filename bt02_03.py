#kiếm tra nhập số từ người dùng có phải là số chẵn hay không
so = int(input("Nhập số nguyên: "))
if so % 2 == 0:
    print(so, "là số chẵn")
else:
    print(so, "không phải số chẵn")
    