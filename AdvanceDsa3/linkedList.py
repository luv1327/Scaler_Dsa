class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(0) 

def generateLinkedList():
    temp = head
    for i in range(10):
        temp.next = Node(i+1)
        temp = temp.next
        
def printAll(head):
    ans = []
    temp = head
    while temp != None:
        ans.append(temp.data)
        temp = temp.next
    print(ans)
    
def size(head):
    temp = head
    count = 0
    while temp != None:
        count +=1
        temp = temp.next
    return count
    
def getKthElement(head,k):
    temp = head
    while k > 0 and temp != None:
        temp = temp.next
        k-=1
    return temp

    

def insertAtTail(head,data):
    length = size(head)
    temp = head
    new_node = Node(data)
    k-=1
    while k > 0 and temp != None:
        temp = temp.next
        k-=1
    new_node.next = temp.next
    temp.next = new_node

def insertAtKth(head,k,data):
    length = size(head)
    if k > length:
        
        return 
    if k == 0:
        return
    temp = head
    new_node = Node(data)
    k-=1
    while k > 0 and temp != None:
        temp = temp.next
        k-=1
    new_node.next = temp.next
    temp.next = new_node


def generateLinkedList(head,A):
    temp = head
    for i in A:
        temp.next = Node(i)
        temp = temp.next
        
def insertAtHead(data):
    global head
    new_node = Node(data)
    new_node.next = head
    head = new_node
    
    


def insertInSortedLinkedList(head,data):
    temp = head

    count = 0
    while temp != None and data > temp.data:
        new_node = Node(data)
        temp = temp.next
        count +=1
    if count > 0:
        temp = getKthElement(head,count-1)
        new_node.next = temp.next
        temp.next = new_node
    else:
        insertAtHead(data)
        
    

generateLinkedList(head,[2,4,9,16,20])
# printAll(head)
# insertInSortedLinkedList(head,-3)
# printAll(head)

def reverse(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
    
def reverseFirstK(head,k):
    if head == None:
        return head
    temp = head
    first = getKthElement(head,k)
    h2 = first.next
    first.next = None
    h1 = reverse(head)
    temp.next = h2
    return h1
    
    

def reverseFirstK(head,k):
    if head == None:
        return head
    h1 = head
    h2 = None
    h3 = head
    i = k 
    while i > 0 and h1 != None:
        temp = h1
        h1 = h1.next
        temp.next = h2
        h2 = temp
        i-=1
    h3.next = reverseFirstK(h1,k)
    return h2
printAll(head)
head = reverseFirstK(head,2)
printAll(head)
        





    

    
    