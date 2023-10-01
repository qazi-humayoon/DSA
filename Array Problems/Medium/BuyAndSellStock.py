#Optimal
#Time Complexity o(N)
#Space Complexity o(1)

prices = [7,1,5,3,6,4]
mini = prices[0]
profit = 0
n = len(prices)
for i in range(n):
    cost = prices[i] - mini
    profit = max(profit,cost)
    mini = min(mini,prices[i])
print(profit)

#_______ ______ ____________  _________________  ________________  ____________________-- ______________  _______________  _______

def stocks(arr,n):
    profit = 0
    mini = prices[0]
    for i in range(n):
        cost = prices[i] - mini
        profit = max(profit,cost)
        mini = min(mini,prices[i])
    return profit

prices = [7,1,5,3,6,4]
n = len(prices)
res = stocks(prices,n)
print(res)
