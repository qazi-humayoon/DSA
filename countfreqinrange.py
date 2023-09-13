
n = 6
x = 9
edges = [1,2,3,1,1,4]

# freq = [0 for _ in range(n)]
    # for i in range(1,n+1):
    #     for j in range(len(edges)):
    #         if edges[j] == i:
    #             freq[i-1] += 1
    # return freq

ans = [0 for _ in range(n)]
for i in range(len(edges)):
    if edges[i] <= n:
        ans[edges[i] - 1] += 1
print(ans)

