#Heap is a complete binary tree with heap order properties

# Heapify is a process used in computer science and algorithms, specifically in the context of heaps, to maintain the heap property or convert an array into a heap data structure.


#Same meaning Max Heap nothing new in it.
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


arr = [ 54, 53, 55, 52, 50]
n = 5

for i in range(n // 2, -1, -1):
    heapify(arr, n, i)

print("Printing the array now:")
for i in range(0, n):
    print(arr[i], end=" ")
print()