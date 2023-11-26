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

    #To do Insertiion in a DLL after a particular Node X
    def add_after(self,data,x):
        if self.head is None: #Checking if the head is empty then the DLL is empty
            print("DLL is empty")
        else: 
            n = self.head #If the DLL is not empty then we traverse in the DLL until N is not None
            while n is not None:
                if x == n.data: #If we get the x after which we want to insert then we break out of the loop otherwise the loop keeps on incrementing
                    break
                n = n.nref
            if n is None: #If Node isn't present in DLL then we print Node isn't present
                print("Node is not present in the Linked List")
            else: #If the node is present in the DLL
                new_node = Node(data) # Creating the new Node withe the help of Node Class
                new_node.nref = n.nref # making the next ref of the old node as the next ref of the new node after which we are going to insert the node in DLL
                new_node.pref = n #Now keeping the ref of previous node in the pref of the new Node to be inserted after a particular node
                while n.nref is not None: #this is mostly used to check if the insertion is not the last node. if the insertion is last node then while wont execute
                    n.nrf.pref = new_node #if its not last node then we change new ref's previous ref to the new_node
                n.nref = new_node #Changing the next ref of the new node

    #Insertion before a particular Node
    def add_before(self,data,x):
        if self.head is None: #Checking if the LL is empty
            print("LL is empty")
        else:
            #Traversing in the DLL to search for the node
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node is not present in the Linked List")
            else:
                new_node = Node(data) #Creating new Node
                new_node.nref = n  #Making the ref of the old next node to new next node
                new_node.pref = n.pref #Making the prev ref of old node to the previous ref of new node
                if n.pref is not None: #This is moslty used to check if we are inserting at the beginning. If that is the case then while loop won't get executed
                    n.pref.nref = new_node #Making the prev ref's new ref as the new node address
                else:
                    self.head = new_node #if it is the first node then storing its ref in the head of the DLL
                    n.pref = new_node

    #Deleting at the beginnig of DLL
    def delete_begin(self):
        if self.head is None: #If the DLL is empty
            print("Linked List is empty")
            return 
        #If the DLL contains only a single Node
        if self.head.nref is None:
            self.head = None
            print("DLL empty after deletion is performed")
        else: #If DLL contains multiple Nodes and changing the head to the head.next ref and making the prev next of new node as None
           self.head = self.head.nref
           self.head.pref = None

    #Deleting the Node at the end of the DLL
    def delete_end(self):
        if self.head is None: #If the DLL is empty
            print("Linked List is empty")
            return
        #If the DLL contains only a single Node
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deletion is performed")
        else:
            #Traversing through the DLL
            n = self.head
            while n.nref is not None:
                n = n.nref 
            n.pref.nref = None #Changing the prev references's next reference to None thus last Node is deleted in DLL

    #Deleting a Node in DLL by Value
    def delete_by_value(self,x):
        if self.head is None: #This is to check if the LL is empty
            print("Linked List is Empty")
            return 
        #This is to check if the LL has only 1 node 
        if self.head.nref is None: 
            if x == self.head.data:
                self.head = None
            else:
                print("Node is not present in the Linked List")
            return 
        #This is used if the node to be deleted is the First Node
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        #This is used if the Node to be deleted is present in the Middle of the Linked List
        n = self.head
        while n.nref is not None:
            if x==n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:  #This else case is used to check if the node to be deleted is the last Node of the Linked List
            if n.data == x:
                n.pref.nref = None
            else:
                print("Node is not present in the DLL")
        



        

dl1 = doublyLL()
# dl1.insert_empty(10)
dl1.add_begin(10)
dl1.add_after(40,10)
dl1.add_before(60,40)
dl1.add_end(30)
# dl1.delete_begin()
dl1.delete_by_value(60)
# dl1.delete_end()
dl1.print_LL()
# dl1.print_LL_reverse()