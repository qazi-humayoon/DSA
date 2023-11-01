#Brute Force
# import math
# def calculateTotalHours(v, hourly):
#     totalH = 0
#     n = len(v)
#     # Find total hours
#     for i in range(n):
#         totalH += math.ceil(v[i] / hourly)
#     return totalH

# def minimumRateToEatBananas(v, h):
#     # Find the maximum number
#     maxi = max(v)

#     # Find the minimum value of k
#     for i in range(1, maxi+1):
#         reqTime = calculateTotalHours(v, i)
#         if reqTime <= h:
#             return i

#     # Dummy return statement
#     return maxi

# v = [7, 15, 6, 3]
# h = 8
# ans = minimumRateToEatBananas(v, h)
# print("Koko should eat at least", ans, "bananas/hr.")

#_________________________________________________________________________________________________________________________

#Optimal Binary search
import math
def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def minimumRateToEatBananas(v, h):
    maxi = max(v)
    low = 1
    high = maxi

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        totalH = calculateTotalHours(v, mid)
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low  #due to o

v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")


