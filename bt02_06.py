input_str = input("Nhập X, Y: ")
dimension = [int(i) for i in input_str.split(",")]
rowNum = dimension[0]
colNum = dimension[1]
multilist = [] 
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = [row]*[col]
print(multilist)