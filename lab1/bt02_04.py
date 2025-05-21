#tạo một danh sách rỗng để lưu kết quả
J = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        #kiểm tra xem số có chia hết cho 7 và không chia hết cho 5 hay không
        #nếu có thì thêm số vào danh sách
        J.append(i)
print(','.join(map(str, J)))