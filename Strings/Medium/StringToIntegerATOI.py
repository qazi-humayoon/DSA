def atoi(s):
    s = s.lstrip()  # Stripping off first left white spaces

    if not s:
        return 0  # if the string has no digits only alphabets then we return 0
    i = 0
    sign = 1
    if s[i] == "+": # if the string has + operater at first
        i += 1
    elif s[i] == "-": # if the string has - operator then we increment by 1 and change the sign also
        i += 1
        sign = -1

    parsed = 0
    while i < len(s):  
        cur = s[i]  # getting the first occurance of the string 

        if not cur.isdigit(): # checking if the string doesn't have digit then we break out of the while loop
            break
        else:
            parsed = parsed * 10 + int(cur) # if there is digit then we calculate until digit's are there
        i += 1                              # E.g 42 -> 0 * 10 + 4 = 4 -> 4 = 4 * 10 + 2 == 42
    parsed *= sign

    if parsed > 2 ** 31 - 1:
        return 2 ** 31 -1
    elif parsed<= -2 ** 31:
        return -2 ** 31
    else:
        return parsed
s = "-42"
res = atoi(s)
print(res)