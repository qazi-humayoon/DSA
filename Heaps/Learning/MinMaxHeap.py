#Heap is a complete binary tree with heap order properties

# Heapify is a process used in computer science and algorithms, specifically in the context of heaps, to maintain the heap property or convert an array into a heap data structure.

# ____________________________________________________________________________
# CAN BE DONE LIKE THIS ALSO
import heapq

min_heap = []
heapq.heappush(min_heap,90)
heapq.heappush(min_heap,60)
heapq.heappush(min_heap,50)
heapq.heappush(min_heap,40)
heapq.heappush(min_heap,35)
print(min_heap)

# ____________________________________________________________________________
# Note
#FOR MAX HEAP CHANGE THE SMALLEST TO LARGEST AND > TO <

def heapify(arr, n, i):
    smallest = i 
    left = 2 * i + 1 #because index starts from 0 if it started from 1 then 2 * i only.
    right = 2 * i + 2

    if left < n and arr[smallest] > arr[left]:
        smallest = left

    if right < n and arr[smallest] > arr[right]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

arr = [ 54, 53, 55, 52, 50]
n = 5

for i in range(n // 2, -1, -1):
    heapify(arr, n, i)

print("Printing the array now:")
for i in range(0, n):
    print(arr[i], end=" ")
print()


#____________________________________________________________________________
#MaxHeap

def heapify(arr,n,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


arr = [54, 53, 55, 52, 50]
n = 5
for i in range(n //2 ,-1,-1):
    heapify(arr,n, i)

print("Printing the arrar now")
for i in range(n):
    print(arr[i],end=" ")
print()