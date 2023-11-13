def checking(num):
    for j in range(len(num) - 1, -1, -1):
        if int(num[j]) % 2 != 0:
            a =  num[0 : j + 1]
            return a

    return ""

num = "35427"
res = checking(num)
print(res)