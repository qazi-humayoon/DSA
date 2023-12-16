# In computer science, a stack is a data structure that follows the Last In, First Out (LIFO) principle.
# This means that the last element added to the stack is the first one to be removed. A stack can be envisioned
# as a collection of elements with two main operations:

# Push: Adds an element to the top of the stack.
# Pop: Removes the element from the top of the stack.
# A stack is often used in situations where the order of processing is important and where the most recently added
# element should be the first to be processed. Think of it like a stack of plates in a cafeteria – you add a plate 
# to the top of the stack, and when you want to take a plate, you take it from the top.

# Key characteristics of a stack:

# LIFO Order: The last element added is the first one to be removed.
# Two Main Operations: Push (to add) and Pop (to remove).
# Top: The position where the last element was added.
# Size: The number of elements in the stack.
# Common use cases for stacks include parsing expressions, function call management (call stack),
# and undo mechanisms in software applications. In programming languages, a call stack is often 
# used to keep track of function calls and returns.

#TC O(N)
# SC O(N)

class Stack:
    def __init__(self):
        self.top = -1       #The top of the stack is always at -1 in the beginning
        self.size = 1000
        self.arr = [0] * self.size  #Making an array with size 1000


    def push(self, x):  #Push the element and before that increment the top by 1 i.e for -1 to 0
        self.top += 1
        self.arr[self.top] = x  #Put the element at the new index in the array


    def pop(self):
        x = self.arr[self.top] #Popping the element only the top elements goes out in stack
        self.top -= 1  #Decreasing the count of the top by 1 as top is deleted
        return x        #Returning the elements which was deleted


    def Top(self):
        return self.arr[self.top]       #To peek at the top element in the stack


    def Size(self):
        return self.top + 1 #To return the size of the stack
    
    def print_stack(self) -> None:  # To print the elements which are present in the stack
        print("Stack elements:", end=" ")
        for i in range(self.top, -1, -1):
            print(self.arr[i], end=" ")
        print()



#Pushing and popping and printing the elements present in the stack
if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    s.print_stack()
    print("Top of stack before deleting any element:", s.Top())
    print("Size of stack before deleting any element:", s.Size())
    s.print_stack()

    popped_element = s.pop()
    print("The element deleted is:", popped_element)

    print("Size of stack after deleting an element:", s.Size())
    print("Top of stack after deleting an element:", s.Top())
    s.print_stack()