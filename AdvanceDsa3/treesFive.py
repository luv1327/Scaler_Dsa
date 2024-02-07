head = None
def convert(root):
    prev = None
    convertHelper(root,prev)
    
def convertHelper(root,prev):
    global head
    if root == None:
        return
    convertHelper(root.left,prev)
    if prev != None:
        root.left = prev
        prev.right = root
    else:
        head = root
    prev = root
    convertHelper(root.right,prev)        