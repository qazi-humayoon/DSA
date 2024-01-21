class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_leaf(root):
    return not root.left and not root.right


def add_left_boundary(root, res):
    cur = root.left
    while cur:
        if not is_leaf(cur):
            res.append(cur.data)
        if cur.left:
            cur = cur.left
        else:
            cur = cur.right


def add_right_boundary(root, res):
    cur = root.right
    tmp = []
    while cur:
        if not is_leaf(cur):
            tmp.append(cur.data)
        if cur.right:
            cur = cur.right
        else:
            cur = cur.left
    for i in range(len(tmp) - 1, -1, -1):
        res.append(tmp[i])


def add_leaves(root, res):
    if is_leaf(root):
        res.append(root.data)
        return
    if root.left:
        add_leaves(root.left, res)
    if root.right:
        add_leaves(root.right, res)


def print_boundary(root):
    res = []
    if not root:
        return res

    if not is_leaf(root):
        res.append(root.data)

    add_left_boundary(root, res)

    # add leaf nodes
    add_leaves(root, res)

    add_right_boundary(root, res)
    return res


def new_node(data):
    node = Node(data)
    return node


if __name__ == "__main__":
    root = new_node(1)
    root.left = new_node(2)
    root.left.left = new_node(3)
    root.left.left.right = new_node(4)
    root.left.left.right.left = new_node(5)
    root.left.left.right.right = new_node(6)
    root.right = new_node(7)
    root.right.right = new_node(8)
    root.right.right.left = new_node(9)
    root.right.right.left.left = new_node(10)
    root.right.right.left.right = new_node(11)

    boundary_traversal = print_boundary(root)

    print("The Boundary Traversal is :", end=" ")
    for i in range(len(boundary_traversal)):
        print(boundary_traversal[i], end=" ")
