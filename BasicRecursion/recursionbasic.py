def funcc(a):
    if a == 5:
        return a
    print(a)
    a+=1
    return funcc(a)


b = 1
result = funcc(b)
print(result)

