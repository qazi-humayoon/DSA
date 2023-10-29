import sys
def findMin(arr: [int]):
    n = len(arr)  # size of the array.
    mini = sys.maxsize
    for i in range(n):
        # Always keep the minimum.
        mini = min(mini, arr[i])
    return mini

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findMin(arr)
    print("The minimum element is:", ans)
