class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
treeroot = TreeNode(100)


def search(root,val):
    while root != None:
        if val > root.val:
            root = root.right
        elif val < root.val:
            root = root.left
        else:
            return True
    return False

def insert(val):
    global treeroot
    root = treeroot
    new_node = TreeNode(val)
    prev = None
    while root != None:
        prev = root
        if val > root.val:
            root = root.right
        else :
            root = root.left
    if root == None:
            return new_node 
    if val > prev.val:
        prev.right = new_node
    else:
        prev.left = new_node
    return root

def traverse(root):
    if root == None:
        return 
    traverse(root.left)
    traverse(root.right)
ans = []
def checkBst(root):
    if root == None:
        return
    checkBst(root.left)
    ans.append(root.val)
    checkBst(root.right)
    
# If ans is sorted, its a bst else not
ans = True
def checkBstRecursive(root,prev):
    global ans
    if root == None:
        return
    checkBstRecursive(root.left,prev)
    if prev != None and prev.val > root.val:
        ans = True
    prev = root
    checkBstRecursive(root.right,prev)
    
def helper(root):
    checkBstRecursive(root,None)
    return ans
    
    
def construct(A,s,e):
    if s > e:
        return None
    mid = (s+e) // 2
    root = TreeNode(A[mid])
    root.left = construct(A,s,mid-1)
    root.right = construct(A,mid+1,e)
    return root

A=[1,2,3,4,5]
construct(A,0,len(A)-1)
    
    



    

    