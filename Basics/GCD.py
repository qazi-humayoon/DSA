a = 11
b = 13
while a > 0 and b > 0:
    if a > b:  #gcd(a-b,b) where a>b (instead of a-b,b we directly find the modulus)
        a = a % b
    else:
        b = b % a
if (a == 0): #if a is 0 then b is the gcd
    print(b)
else:
    print(a) #else if b is 0 then a is the gcd