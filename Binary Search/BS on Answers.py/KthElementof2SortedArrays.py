#Recheck because the concept was not clear

def kthelement(array1, array2, m, n, k):
    p1 = 0
    p2 = 0
    counter = 0
    answer = 0


    while (p1 < m and p2 < n):
        if (counter == k):
            break
        elif (array1[p1] < array2[p2]):
            answer = array1[p1]
            p1 += 1
        else:
            answer = array2[p2]
            p2 += 1
        counter += 1
    if (counter != k):
        if (p1 != m-1):
            answer = array1[k-counter]
        else:
            answer = array2[k-counter]
    return answer




if __name__ == "__main__":
    array1 = [2, 3, 6, 7, 9]
    array2 = [1, 4, 8, 10]
    m = len(array1)
    n = len(array2)
    k = 5
    print("The element at the kth position in the final sorted array is",
          kthelement(array1, array2, m, n, k))