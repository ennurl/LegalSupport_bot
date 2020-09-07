id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

block = int(len(id) // 5)
start_block = 0

for i in range(block):
    print(id[0+start_block:5*(i+1)])
    start_block += 5

end_blocl = 5 * block
print(id[end_blocl:len(id)])

