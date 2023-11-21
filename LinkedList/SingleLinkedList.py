class Node: 
    #creating nodes in this class 
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    #class used for travesing the data in the linked list
    def __init__(self):
        #At the beginning the linked list will be empty so the head will also not contain anything.
        self.head = None
    def print_LL(self): 
        #If head is empty that means the linked list is also empty.
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                #Here it prints the data that is present in the linked list
                print(n.data,"-->", end = " ")
                n = n.ref

    #in this function we are adding the node at the beginning 
    def add_begin(self,data):
        #Here we just create a node using Node class
        new_node = Node(data)
        #Here we put the reference of the beginning head equal to the reference of the new node we created
        new_node.ref = self.head
        #Now the new node reference/link is to be stored in head. That is what we are doing here in this.
        self.head = new_node
    
    #in this function we are adding the node at the end 
    def add_end(self,data):
        #Here we just create a node using Node class
        new_node = Node(data)
        #Here we check that if the linked list is empty, then the node we are inserting at the end will become the first node
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            #since we are inserting at the end then means ref/link will be null not untill it is not null we will traverse.
            #Since we traverse till last node bcz we are inserting at the end
            while n.ref is not None:
                #here n.ref is used to go to all the references until it ref becomes none
                n = n.ref
                #once it is none then new_node ref is putted in this reference and new_node refernce will be equal to none as it will be the last node
            n.ref = new_node
    
    #In this function we are adding the node in between two nodes.
    #But there is a catch i.e is we have to specify whether it is before or after a particular node or not
    def add_after(self,data,x):
        n = self.head
        #just like here im searching for that node using x and n.data to see if the node is there or not
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the linked list")
        else:
            #Here in this else im changing the reference of the nodes and putting new node after that partcular selected node
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

#     #adding the element before a node. here a conditons raises that a node can be a which can come before the first node. so that new node becomes the first node now.
    def add_before(self,data,x):
        # here we are checking if the linked list is empty or there are elements present in it.
        if self.head is None:
            print("Linked List is empty!")
            return
        # here we are checking if the x element is present in the linked list or not.
        if self.head.data==x:
            # if it is present then we will simply insert as we do while inserting at the beginning. Check above how insertion at beginning is done.
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        #here in this part we will add nodes between rest of the parts apart from the beginning
        n = self.head
        # while loop is used to check the previous node the the x. i.e if linkedlist is 1-2-3 and if x is 3 then previous node is 2. REFER NOTES
        while n.ref is not None:
            #here we check if the next node is equal to the x value before which we are doing insertion
            if n.ref.data==x:
                # if the node is present then break the statement
                break
            # it is used to traverse to the next elements through the nodes as we do in linked lists
            n = n.ref        
        if n.ref is None:
            print("Node is not found!")
        else:
            # here everything is similar to the previous method i.e add_after 
            # here we are creating a new node using node class
            new_node = Node(data)
            # we put the new node ref equal to the old node ref
            new_node.ref = n.ref
            # old node will keep the refrence of the new node
            n.ref = new_node  
    
        # we use this to insert node in the linked list if it is empty.
    def insert_empty(self,data):
        # here we check if the linked list is empty or not
        if self.head is None:
            # if it is empty then we will create a new node 
            new_node = Node(data)
            #assign the head which initially is zero to the new_node
            self.head = new_node
        else:
            #if the linked list is not empty then print not empty
            print("Linked list is not empty")
    
            # deleting the node present at the beginning of the linked list 
    def delete_begin(self):
        # we are checking if the linked list is empty or not if yes then print linked list is not empty
        if self.head is None:
            print("Linked list is empty can't delete any node")
        else:
            # here self.head contains the ref of the 1st node
            # self.head.ref is the 1st node which contains the ref of the 2nd node
            # thus here we assing self.head equal to 2nd node whose reference is present in the 1st node in self.head.ref
            self.head = self.head.ref

            # Here we delete the element at the end
    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.ref is None: #checking if it has only 1 node that has none then delete that and make head none
            self.head = None #Self.head.ref gives us the reference which is present in the first node
        else: 
            n = self.head
            while n.ref.ref is not None: #here we search for the ref ref ie from one node ref to other node
                n = n.ref #Self.ref.ref gives use the ref of the other node
            n.ref = None

                #Deleting the Node at any place in the Linked List
    def delete_by_value(self,x):
        if self.head is None: #Checking if the linked list is empty or not if it is then print it is empty and return it
            print("Linked List is empty cant delete")
            return
        if x == self.head.data:  #Checking if the x is first node if that is the case then we simply change the ref of head to the 2nd node using n.head.ref and return
            self.head = self.head.ref
            return
        n = self.head
        while n is not None: #Checking the previous node which comes just before that node which is to be deleted
            if x == n.ref.data: #Checking is the x is equal to the node which is to be deleted n.ref.data tells if the next node is equal to x or not if it is then we break
                break
            n = n.ref #It is used to move forward in the linked list as it contains the ref of the other nodes
        if n.ref is None:  #If n.ref is still none that means the node is not present in the linked list
            print("Node isnt present")
        else:
            n.ref = n.ref.ref #if the node is present in the linked list then we change the ref of the linked list with the ref of the node which the node to be deleted contains


    


LL1 = LinkedList()
LL1.add_begin(10)
# LL1.add_end(100)
# LL1.add_before(600,10)   #adding 600 before 10
# LL1.add_after(700,600)   #we are adding 700 after 600
LL1.add_begin(15)
LL1.add_begin(19)
# LL1.delete_end()  #Delete the node at the last
LL1.delete_by_value(15) #Deleting the node at any place in linked list
# LL1.insert_empty(10) #Note :- Here insert_empty won't add 10 because there are already nodes present in the linked list
# LL1.delete_begin()   #here it should be used at last if used earlier and adding after that it will show not empty. here we are deleting at the beginning
LL1.print_LL()         #printing the whole linked list     