def comparison(a, b):
    return a[2] > b[2]

def job_scheduling(arr, n):
    arr.sort(key=lambda x: x[2], reverse=True)
    maxi = max(job[1] for job in arr)

    slot = [-1] * (maxi + 1)
    count_jobs = 0
    job_profit = 0

    for i in range(n):
        for j in range(arr[i][1], 0, -1):
            if slot[j] == -1:
                slot[j] = i
                count_jobs += 1
                job_profit += arr[i][2]
                break

    return count_jobs, job_profit


if __name__ == "__main__":
    n = 4
    arr = [(1, 4, 20), (2, 1, 10), (3, 2, 40), (4, 2, 30)]

    ans = job_scheduling(arr, n)
    print(ans[0], ans[1])
