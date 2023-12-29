= 1
b = 1
c = 0
num = int(input())
if num == 1 or num == 2:
    print("1")
for i in range(2,num):
    c = a + b
    a = b
    b = c
    print(b,end=" ")