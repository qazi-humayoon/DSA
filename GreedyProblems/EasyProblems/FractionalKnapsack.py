def compare(a):
    return a[1] / a[0]

def maximumValue(items, n, w):
    # Sort items according to value/weight.
    items = sorted(items, key=compare, reverse=True)

    maxValue = 0
    currWeight = 0

    for i in range(n):
        if currWeight + items[i][0] <= w:
            currWeight += items[i][0]
            maxValue += items[i][1]
        else:
            remainingWeight = w - currWeight

            # Pick a fraction of the current item.
            maxValue += items[i][1] * (remainingWeight / items[i][0])
            break

    return round(maxValue, 2)

if __name__ == "__main__":
    n = 3
    w = 50
    items = [(20, 100), (10, 60), (30, 120)]

    result = maximumValue(items, n, w)
    print(f"The maximum value is {result}")
