from collections import deque

def search(root,val):
    if root == None:
        return False
    if root.data == val:
        return True
    return search(root.left,val) or search(root.right,val)

def generatePath(root,val,path):
    if root == None:
        return False
    path.append(root.data)
    if root.data == val:
        return True
    if generatePath(root.left,val,path) or generatePath(root.right,val,path):
        return True
    path.pop()
    return False

def findLca(root,a,b):
    pathOne = []
    pathTwo = []
    generatePath(root,a,pathOne)
    generatePath(root,b,pathTwo)
    i = 0
    num = -1
    while i < len(pathOne) and i < len(pathTwo):
        if pathOne[i] == pathTwo[i]:
            num = pathOne[i]
        i+=1
    return num
    


def findLcaBst(root,a,b):
    while root != None:
        if root.data > a and root.data > b:
            root = root.left
        elif root.data < a and root.data < b:
            root = root.right
        else:
            return root
    return None

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

def connectNodesAtSameLevel(root):
    if root == None:
        return root
    q = deque()
    q.append(root)
    last = q[0]
    while len(q) > 0:
        first = q[0]
        q.popleft()
        if first.left:
            q.append(first.left)
        if first.right:
            q.append(first.right)
        if first == last:
            first.next = None
            if len(q) > 0:
                last = q[-1]
        else:
            first.next = q[0]
            
def findKdistanceNode(root,k):
    if root == None:
        return
    if k == 0:
        print(root.data)
    findKdistanceNode(root.left,k-1)
    findKdistanceNode(root.right,k-1)
    

