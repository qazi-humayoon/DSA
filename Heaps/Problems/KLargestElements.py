#Check Love Babbar video or notes . same logic for smallest but have to maintain the Max-Heap which idk how do in python using heapq libraray. python maintains min heap by default in heapq library

import heapq
def kLargest(lst, k):
    n = 5
    ans = []
    min_heap = []

    for i in range(k):
        heapq.heappush(min_heap, lst[i])

    for i in range(k, n):
        if min_heap[0] < lst[i]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, lst[i])

    while min_heap:
        ans.append(heapq.heappop(min_heap))

    return ans