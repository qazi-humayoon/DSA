class MinStack:
    def __init__(self):
        self.st = []

    def push(self, x):
        if not self.st:
            minimum = x
        else:
            minimum = min(self.st[-1][1], x)    #Getting the last element pair and last element of that pair minimum
        self.st.append((x, minimum))        #Appending that pair in the stack st

    def pop(self):
        self.st.pop()

    def top(self):
        return self.st[-1][0]

    def getMin(self):
        return self.st[-1][1]

# Example usage:
minStack = MinStack()
minStack.push(3)
minStack.push(5)
print("Minimum:", minStack.getMin())  # Output: 3
minStack.push(2)
print("Minimum:", minStack.getMin())  # Output: 2
minStack.pop()
print("Top:", minStack.top())          # Output: 5
print("Minimum:", minStack.getMin())  # Output: 3
