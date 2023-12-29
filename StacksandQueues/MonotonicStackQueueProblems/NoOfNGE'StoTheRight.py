def nextnge(arr,query,N,Q):
    st = []
    for i in query:
        cnt = 0
        for j in range(i + 1,N):
            if arr[i] < arr[j]:
                cnt += 1
        st.append(cnt)

    return st

arr = [1, 3, 6, 5, 8, 9, 13, 4]
N=8
Q=3
query = [0, 1, 5]

ans = nextnge(arr,query,N,Q)
print(ans)