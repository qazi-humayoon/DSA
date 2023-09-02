n = 336
temp = n
count = 0
while(temp != 0):
    c = temp % 10
    temp //= 10
    if c > 0 and n % c==0:
            count += 1
    
print(count) 