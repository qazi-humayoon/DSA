class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_l(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n:
                print(n.data,"-->",end="")
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
#_________________________________________________________________________________________

#Finding the Middle Node Brute Approach TC: O(N) SC: O(1)
    def counting1(self):
        cnt = 0
        n = self.head
        while n:
            cnt += 1
            n = n.ref
        n = self.head
        for i in range(cnt//2):
            n = n.ref
        return n

#_________________________________________________________________________________________

#Finding the Middle Node Optimal Approach TC: O(N) SC: O(1)
    def counting(self):
        slow = self.head
        fast = self.head
        while fast and fast.ref:
            slow = slow.ref
            fast = fast.ref.ref
        return slow
#_________________________________________________________________________________________
LL1 = LinkedList()
LL1.add_begin(50)
LL1.add_begin(40)
LL1.add_begin(30)
LL1.add_begin(20)
LL1.add_begin(10)
LL1.print_l()
    
Middle = LL1.counting()
print("\nMiddle Node Using Turtle and Hare Approach :",Middle.data)

Middle1 = LL1.counting1()
print("Middle Node Using Brute :",Middle1.data)
            