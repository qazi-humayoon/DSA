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
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(15)
LL1.print_LL()








#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref