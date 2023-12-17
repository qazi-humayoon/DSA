# TC O(N)
# SC O(2N)

#Less Efficient using Two Stacks
from queue import LifoQueue
# using LifoQueue which is a stack in python
class Queue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()


    def push(self, data: int) -> None:
        # Pop out all elements from the stack input
        while not self.input.empty():
            self.output.put(self.input.get())
        # Insert the desired element in the stack input
        print("The element pushed is", data)
        self.input.put(data)
        # Pop out elements from the stack output and push them into the stack input
        while not self.output.empty():
            self.input.put(self.output.get())


    # Pop the element from the Queue
    def pop(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        val = self.input.get()
        return val


    def Top(self) -> int: 
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        return self.input.queue[-1]


    def size(self) -> int:
        return self.input.qsize()




if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())

#__________________________________________________________________________________________________________________________

# TC O(1)
# SC O(2N)

#Efficient Sol using Two Stacks
class QueueUsingStacks:

    def __init__(self) -> None:
        self.enqueue_stack = []   # Stack for enqueue operations
        self.dequeue_stack = []   # Stack for dequeue operations

    def enQueue(self, val: int) -> None:
        # Push the element onto the enqueue stack
        self.enqueue_stack.append(val)

    def deQueue(self) -> int:
        # Check if dequeue stack is empty, then transfer elements
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        # Pop from dequeue stack (front of the queue)
        if self.dequeue_stack:
            return self.dequeue_stack.pop()
        else:
            return -1  # Indicates an empty queue

    def peek(self) -> int:
        # Check if dequeue stack is empty, then transfer elements
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        # Peek at the front of the queue without removing the element
        if self.dequeue_stack:
            return self.dequeue_stack[-1]
        else:
            return -1  # Indicates an empty queue

    def isEmpty(self) -> bool:
        # Check if both stacks are empty
        return not self.enqueue_stack and not self.dequeue_stack

# Example usage:
if __name__ == "__main__":
    # Create a queue using stacks
    q = QueueUsingStacks()

    # Enqueue some elements
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    # Print the queue
    print(f"Queue: {q.dequeue_stack[::-1] + q.enqueue_stack}")

    # Peek at the front of the queue
    front_element = q.peek()
    print(f"Front of the queue: {front_element}")

    # Dequeue elements
    dequeued_element = q.deQueue()
    print(f"Dequeued element: {dequeued_element}")

    # Print the updated queue
    print(f"Updated Queue: {q.dequeue_stack[::-1] + q.enqueue_stack}")
