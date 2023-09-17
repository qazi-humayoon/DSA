
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        quickSort(arr, low, pIndex - 1)
        quickSort(arr, pIndex + 1, high)

def main():
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    n = len(arr)
    
    print("Before Using Quick Sort:")
    for i in range(n):
        print(arr[i], end=" ")
    print()
    
    quickSort(arr, 0, n - 1)
    
    print("After Using Quick Sort:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    main()
