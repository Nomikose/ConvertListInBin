
List = [2, 1, -99, -115, -4, 54, 9, 78, -58, -2, 27, 0, 0, 17, -124, 123, 117, 63, 100, 97, 30, -35, 79, -38, -54, -54, 110, 27, -21, 68, 21, -89, -1, -1, -1, 8, -116, 53, 0, 0, 0, -63, 64]
f = open('myfile3.bin', 'wb')
for item in List:
    s = str(item) + '\n'
    bt = s.encode()
    f.write(bt)
f.close();
L2 = []
f = open('myfile3.bin', 'rb')
for ln in f:
    x = int(ln)
    L2 = L2 + [x]

print("L2 = ", L2)
f.close();