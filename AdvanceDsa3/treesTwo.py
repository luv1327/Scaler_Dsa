from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    ans = []
    q = deque()
    if root == None:
        return ans
    q.append(root)
    while len(q) > 0:
        top = q[0]
        q.popleft()
        ans.append(top.data)
        if top.left:
            q.append(top.left)
        if top.right:
            q.append(top.right)
    return ans

def printByLevel(root):
    if root == None:
        return 
    q = deque()
    q.append(root)
    last = q[0]
    ans = []
    temp = []
    while len(q) > 0:
        first = q[0]
        q.popleft()
        temp.append(first.data)
        if first.left:
            q.append(first.left)
        if first.right:
            q.append(first.right)
        
        if first == last:
            temp = []
            if len(q) > 0:
                last = q[-1]
                
def leftSideView(root):
    if root == None:
        return
    q = deque()
    ans = []
    q.append(root)
    first = q[0]
    while len(q) > 0:
        top = q[0]
        q.popleft()
        if top.left:
            q.append(top.left)
        if top.right:
            q.append(top.right)
        if top == first:
            ans.append(top.data)
            if len(q) > 0:
                first = q[0]

def rightSideView(root):
    if root == None:
        return
    q = deque()
    q.append(root)
    last = q[0]
    ans = []
    while len(q) > 0:
        top = q[0]
        q.popleft()
        if top.left:
            q.append(top.left)
        if top.right:
            q.append(top.right)
        
        if last == top:
            ans.append(top.data)
            if len(q) > 0:
                last = q[-1]
                
def inOrderTraversal(root):
    if root == None:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)
    
root = None
five = TreeNode(5)
seven = TreeNode(7)
nine = TreeNode(9)
root = five
root.left = seven
root.right = nine
three = TreeNode(3)
two = TreeNode(2)
seven.left = three
seven.right = two
six = TreeNode(6)
nine.right = six


def iterativeInOrderTraversal(root):
    stack = []
    ans = []
    while len(stack) > 0 or root != None:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            last = stack[-1]
            stack.pop()
            ans.append(last.data)
            root = last.right
    return ans

print(iterativeInOrderTraversal(root))

        

    

        
    
    
    
