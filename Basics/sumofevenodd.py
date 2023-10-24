n = int(input())
val1 = 0
val2 = 0
while n > 0:
    a = n % 10
    if a % 2 == 0:
        val1 += a
    else:
        val2 += a
    n //= 10
print(val1," ",val2)
