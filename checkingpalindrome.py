# Convert the integer into the string and then slice the string and then store that
#  string back in the x integer. | Simple method to do it |
x = str(x)
return x == x[::-1] #comparing the string with opposite of the string 
# basically we are checking two strings here if they are same or not.

x = 1221
if x < 0 or (x!=0 and x % 10 == 0):
    print("false")
half = 0
while (x > half):
    c = x % 10
    half = (half*10) + c
    x //= 10
if x == half or x == half // 10:
    print("true")


