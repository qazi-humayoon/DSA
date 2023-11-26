class Node: #Creating the Nodes here using the Node class
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:
    #At the initial the head is always going to to empty so we keep it None
    def __init__(self):
        self.head = None

    #Traversing in the doubly LL we check if the head is None if it's None we print LL is empty if it's not empty then we traverse in the LL until n is not None
    def print_LL(self): 
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data,"-->",end="")
                n = n.nref

    #for the reverse traversal in doubly LL we again check if LL is empty or not and then check n.nref which is next reference 
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:  #If the next reference is none we just move forward without printed so that we can move in backward in later stage to backwared traversal
                n = n.nref
            while n is not None: #Checking until n is not none and traversing with the help of previous reference
                print(n.data,"-->",end="")
                n = n.pref
    #Checking if the LL is empty. If it is empty we then insert the node in the LL
    def insert_empty(self,data):
            if self.head is None:
                new_node = Node(data)
                self.head = new_node
            else:
                print("Linked List is not empty!")

    #Inserting at the beginning of the LL
    def add_begin(self,data):
            new_node = Node(data) #Creating the node first for insertion at the beginning
            if self.head is None: #Checking if the LL is empty it that is the case then making the Node first Node in LL
                self.head = new_node
            else:       #If the Node is not empty then we inserting at the beginning
                new_node.nref = self.head  #first storing ref in head in the new_node nextref
                self.head.pref = new_node #then storing the reference of new_node in the head of previous node
                self.head = new_node        #at last storing the ref of the new_node in the head

    #Inserting at the end of the LL
    def add_end(self,data):
            new_node = Node(data) #Creating the node first for insertion at the beginning
            if self.head is None: #Checking if the LL is empty it that is the case then making the Node first Node in LL
                self.head = new_node
            else:        #If the Node is not empty then we inserting at the end.
                n = self.head
                while n.nref is not None: #Traversing until the next ref is not none
                    n = n.nref   #with the help of this we can move on to the next node
                n.nref = new_node       # Storing the ref of new_node in the next ref of the previous node
                new_node.pref = n       # Storing the ref of the prev node in the new_node previous reference

    def add_after(self,data,x):
        if self.head is None:
            print("DLL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node is not present in the Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                while n.nref is not None:
                    n.nrf.pref = new_node
                n.nref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node is not present in the Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                    n.pref = new_node

            
        

dl1 = doublyLL()
# dl1.insert_empty(10)
dl1.add_begin(10)
dl1.add_after(40,10)
dl1.add_before(60,40)
dl1.add_end(30)
dl1.print_LL()
# dl1.print_LL_reverse()