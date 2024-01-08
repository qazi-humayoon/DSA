def heapsort(arr, n):
    size = n

    while size > 1:
        arr[size - 1], arr[0] = arr[0], arr[size - 1]
        size -= 1
        heapify(arr, size, 0)

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

arr = [54, 53, 55, 52, 50]
n = 5

for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

heapsort(arr, n)

print("Printing the array now:")
for i in range(0, n):
    print(arr[i], end=" ")
print()
