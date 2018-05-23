class BinaryTreeNode(object):
    #__slots__= ['value', 'left', 'right']
    def __init__(self, value, left=None, right=None):
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    '''
    Input: root - root node of the binary search tree
    Output: True or False depending on whether the Binary Tree is a "Super Tree"
    Axioms: 
        1 - Root can be null
        2 - Root can have no children
        3 - We only need to find two leaf nodes that don't fit "Super Tree" requirement to return False
    Approach:
        1 - Check if root is null, if so return True because it technically fits Super Tree requirements
        2 - Add the root to a list stack called "nodes" where we will add all nodes we come across and check if whether they are a leaf node or not
        3 - We perform a loop while our nodes list is not empty and we will check if every node in their is a leaf node or not
        4 - If we find a leaf node, we check if its depth is in our list of depths and if it is we do nothing, if not we add it to our list
        5 - We then check whether our list is greater than 2 or if it is equal to two and its two values are seperated by more than 1. If either condition is true we return False
        6 - If the node we are looking at is not a leaf node, we add its children to our node list and repeat the cycle.
        7 - If we make it through all of our leaf nodes and don't find any errors, we return True
    '''

    def is_super_tree(root):
        if root == None:
            return True
        leaf_depths = []
        
        nodes = []
        nodes.append((root, 0))
        
        while len(nodes) > 0:
            node, depth = nodes.pop()
            
            if node.left == None and node.right == None:
                if depth not in leaf_depths:
                    leaf_depths.append(depth)
                    if len(leaf_depths) > 2 or len(leaf_depths) == 2 and (abs(leaf_depths[0] - leaf_depths[1]) > 1):
                        return False
            
            else:
                if node.left:
                    nodes.append((node.left), depth + 1)
                if node.right:
                    nodes.append((node.right), depth + 1)
                    
        return True
        
