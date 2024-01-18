# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None



#     def show(self):
#         if self.left:
#             self.left.show()

#         print(self.data)

#         if self.right:
#             self.right.show()



# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.show() 


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def show(self):
        if self.left:
            self.left.show()
        print(self.data)

        if self.right:
            self.right.show()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(9)

root.show()
        