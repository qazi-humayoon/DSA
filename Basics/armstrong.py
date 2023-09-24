n = 1
temp = n
l = len(str(n))
count = 0
while temp != 0:
    c = temp % 10
    count += c**l
    temp //= 10
if count == n:
    print("True")
else:
    print("False")

