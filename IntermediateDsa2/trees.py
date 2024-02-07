class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        

def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def size(root):
    if root == None:
        return 0
    left_height = size(root.left)
    right_height = size(root.right)
    return left_height + right_height + 1

def sumOfAllNodes(root):
    if root == None:
        return 0
    left_sum = sumOfAllNodes(root.left)
    right_sum = sumOfAllNodes(root.right)
    return left_sum + right_sum + root.data


def heightOfATree(root):
    if root == None:
        return 0
    left_height = heightOfATree(root.left)
    right_height = heightOfATree(root.right)
    return max(left_height,right_height) + 1