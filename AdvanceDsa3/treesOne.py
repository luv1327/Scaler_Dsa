def preOrder(root):
    if root == None:
        return 
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
def calculateSize(root):
    if root == None:
        return 0
    return root.left + root.right + 1

def calculateSumOfAll(root):
    if root == None:
        return 0
    left =  calculateSumOfAll(root.left)
    right = calculateSumOfAll(root.right)
    return left + right + root.data

def calculateHeight(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 0
    l = calculateHeight(root.left)
    r = calculateHeight(root.right)
    return max(l,r) + 1

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0

def buildDepth(root,depth):
    if root == None:
        return
    root.depth = depth 
    buildDepth(root.left,root.depth + 1)
    buildDepth(root.right,root.depth + 1)