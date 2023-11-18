def reverseword(s):
    m = s.split()
    reversed_str = ' '.join(m[::-1])
    return reversed_str


s = "the sky is blue"
res = reverseword(s)
print(res)