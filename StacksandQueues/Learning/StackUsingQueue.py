'''
# STACK USING QUEUE WITH THE HELP OF TWO QUEUES CHECK NOTES OR STRIVER ARTICLES/VIDEO
    Time complexity: O(Q*N)
    For each push operation O(N); O(1) for all other operations.
    
    Space complexity: O(max(N1, N2))

    where Q is the number of queries, N denotes the maximum number of elements in the queue and
    'N1' and 'N2' denote the size of queues 'q1' and 'q2'.
'''
from collections import deque


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def getSize(self) -> int:
        # Return the size of the queue 'q1'.
        return len(self.q1)

    def isEmpty(self) -> bool:
        return self.getSize() == 0

    def push(self, element: int) -> None:
        # Simply enqueue data to q1.
        self.q1.append(element)

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        # Enqueue all the elements of q1 into q2 except the last one.
        while len(self.q1) > 1:
            self.q2.append(self.q1[0])
            self.q1.popleft()

        # Last element of q1 is our answer.
        ans = self.q1[0]
        self.q1.popleft()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return ans

    def top(self) -> int:
        if self.isEmpty():
            return -1

        # Enqueue all the elements of q1 into q2 except the last one.
        while len(self.q1) > 1:
            self.q2.append(self.q1[0])
            self.q1.popleft()

        ans = self.q1[0]
        self.q1.popleft()
        self.q2.append(ans)
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return ans
#_________________________________________________________________________________________________________________________________

# STACK USING QUEUE WITH THE HELP OF SINGLE QUEUES CHECK NOTES OR STRIVER ARTICLES/VIDEO
# TC : O(N)
# SC : O(N)
class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.q = []

    def push(self, x):
        # Push a new element onto the stack

        # Append the new element to the end of the list
        self.q.append(x)  #IN CODING PLATFORMS WRITING THIS MUCH IS ENOUGH

        # Rearrange the elements to reverse the order (simulate stack behavior)
        for _ in range(len(self.q) - 1):
            # Dequeue each element from the front and immediately enqueue it at the rear
            self.q.append(self.q.pop(0))

    def pop(self):
        # Pop the top element from the stack (front of the list)

        # Return None if the stack is empty
        return self.q.pop(0) if self.q else None #ADD ELSE -1 IN CODING PLATFORMS

    def top(self):
        # Return the top element of the stack without removing it

        # Return None if the stack is empty
        return self.q[0] if self.q else None    #ADD ELSE -1 IN CODING PLATFORMS

    def size(self):
        # Return the size (number of elements) of the stack
        return len(self.q)
    
    def is_empty(self):
        return not self.q   #TO CHECK IF STACK IS EMPTY OR NOT
    
    def print_elements(self):
        # Print all elements in the stack
        print("Elements in the stack:", end=" ")

        # Iterate through the elements and print each one
        for i in range(self.size()):
            print(self.q[i], end=" ")

        print()  # Print a newline for better formatting


# Main function
if __name__ == "__main__":
    # Create a stack instance
    s = Stack()

    # Push elements onto the stack
    s.push(3)
    s.push(2)
    s.push(4)
    s.push(1)
    s.print_elements()
    # Print the top element of the stack
    print("Top of the stack:", s.top())

    # Print the size of the stack before removing an element
    print("Size of the stack before removing element:", s.size())

    # Pop an element from the stack
    print("The deleted element is:", s.pop())

    # Print the top element of the stack after removing an element
    print("Top of the stack after removing element:", s.top())

    # Print the size of the stack after removing an element
    print("Size of the stack after removing element:", s.size())
