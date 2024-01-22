#Some issues in it while running here but works fine in leetcode or coding ninjas

from collections import deque, defaultdict

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def verticalTraversal(root):
    if not root:
        return []

    # Dictionary to store nodes for each column
    columns = defaultdict(list)

    # Queue for level-order traversal
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()

        # Store the node in the corresponding column
        columns[col].append((row, node.val))

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    # Sort nodes within each column by row and value
    result = []
    for col in sorted(columns.keys()):
        column_data = columns[col]
        column_data.sort(key=lambda x: (x[0], x[1]))
        result.append([val for _, val in column_data])

    return result

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

verticalOrderTraversal = verticalTraversal(root)
print(verticalOrderTraversal)
