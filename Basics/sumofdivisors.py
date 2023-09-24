# n = 5
# count = 0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += j
# print(count)

# n = 4
# ans = 0
# l = 1

#     # Iterating over all values of 'l' such that 'n/l' is distinct.
#     # There at most 2*sqrt(n) such values.
# while l <= n:
#     val = n // l

#         # 'r' = maximum value of 'i' such that 'n/i' is val.
#     r = n // val
#     ans += ((r * (r + 1)) // 2 - (l * (l - 1)) // 2) * val
        
#         # moving on to next range.
#     l = r + 1

# print(ans)
n = 5
ans = 0

    # Iterating over all 'i'. Each 'i' contributes to final answer
    # exactly 'floor(n/i)' times.
for i in range(1, n+1):
    ans += i * (n // i)

print(ans)

    

