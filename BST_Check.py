class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        

'''
Input: A root node of a tree
Output: True or False depending on whether not the tree is true or not
Axioms: 
    1 - Root node can be empty
    2 - Root node can have no children
    3 - Duplicates are allowed
    4 - Negatives are allowed
    5 - Size negligable
    
Approach:
    1 - We will check if there is a root node, if not we pass True
    2 - If our root node has no children we also return True
    3 - Next we will perfom a BFS on our Binary Tree and as we find every node, we add them to a queue list of nodes
    4 - We keep a loop running till our queue is empty
    5 - For each node we check if its children's values are in their corresponding positions, if not, we return False
    6 - Once we are checking a node, we make sure to pop it out to avoid repeating the same checks.
    7 - If we are at a leaf node, we skip it
    8 - If we manage to go through all of the nodes without an error, we return True
    
'''
def bst_check(root):
    # write the body of your function here
    if root is None or root.left is None and root.right is None:
        return True
    nodes = []
    nodes.append((root, float("-inf"), float("inf")))
    
    while len(nodes):
        node, min_val, max_val = nodes.pop()
        if node.left:
            if node.left.value > node.value or node.left.value < min_val:
                return False
            else:
                nodes.insert(0,(node.left, min_val, node.value))
        if node.right:
            if node.right.value < node.value or node.right.value > max_val:
                return False
            else:
                nodes.insert(0,(node.right, node.value, max_val))

    return True
