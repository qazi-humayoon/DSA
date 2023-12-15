#  A queue is a data structure that follows the First-In-First-Out (FIFO) principle, which means that the first element added to the queue will be the first one to be removed. Imagine a real-life queue, like people waiting in line; the person who arrives first is the first one to be served.

# Here are some key points about queues that you can discuss in an interview:

# Basic Operations:

# Enqueue (Push): Adding an element to the end (rear) of the queue.
# Dequeue (Pop): Removing the element from the front (front) of the queue.
# Front: The front is the first element in the queue, the one that will be dequeued next.
# Rear (or Back): The rear is the last element in the queue, the one that was enqueued most recently.
# Real-life Analogy:

# Compare a queue to a line of people waiting for a bus or at a ticket counter. The person who arrives first gets in the front of the line 
# and is the first to be served.
# Use Cases:

# Queues are used in various computing scenarios, such as task scheduling, order processing, and managing resources in a way that ensures fairness.
# Implementation:

# Queues can be implemented using arrays or linked lists. The implementation you provided earlier is an example of a circular queue using an array.
# Applications:

# Breadth-First Search (BFS): Queues are often used in algorithms like BFS, where you explore all neighbors of a node before moving on to the next level.
# Print Queue: In a printer, the documents are printed in the order they are sent to the print queue.
# Task Scheduling: Queues are used in operating systems to manage tasks waiting for execution.
# Complexity:

# Enqueue and dequeue operations in a basic queue implemented with an array or linked list have a time complexity of O(1).
# Circular Queue:

# In scenarios where you want to efficiently use the available space in the array and avoid unnecessary shifting, a circular queue can be implemented.
# Overflow and Underflow:

# Overflow occurs when trying to enqueue an element into a full queue, and underflow occurs when trying to dequeue from an empty queue.
# Thread Safety:

# In a multi-threaded environment, it's crucial to implement thread-safe operations on a queue to prevent data corruption.
# Priority Queues:

# Priority queues are a variation where each element is assigned a priority, and the element with the highest priority is served before others.
class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0] * self.maxSize


    def push(self, newElement):
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        self.arr[self.end] = newElement
        print("The element pushed is", newElement)
        self.currSize += 1


    def pop(self):
        if self.start == -1:
            print("Queue Empty\nExiting...")
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return popped


    def top(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]


    def size(self):
        return self.currSize




if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())