class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
        
head = None
tail = None
count = 0

def printAll(head):
    ans = []
    temp = head
    while temp != None:
        ans.append(temp.value)
        temp = temp.next
    print(ans)

def insertAtEnd(value):
    global head
    global tail
    new_node = Node(value)
    if head == None and tail == None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        new_node.prev = tail
        tail = tail.next

def deleteFromFront():
    global head
    global tail
    if head == tail:
        head = None
        tail = None
    else:
        head = head.next
        head.prev = None
        
def deleteFromBack():
    global head
    global tail
    if head == tail:
        head = None
        tail = None
    else:
        tail = tail.prev
        tail.next = None
    
    
def deleteByRef(node):
    global head
    global tail
    if node.next == None:
        deleteFromBack()
    elif node.prev == None:
        deleteFromFront()
    else:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    
def deleteByValue(value):
    global head
    temp = head
    while temp != None:
        if temp.value == value:
            break
        temp = temp.next
    if temp:
        deleteByRef(temp)
        
def deleteQueries(Q):
    n = len(Q)
    hm = {}
    global head
    temp = head
    while temp != None:
        hm[temp.value] = temp
        temp = temp.next
    for i in range(n):
        deleteByRef(hm[Q[i]])
    


def lruCache(A,capacity):
    global count
    global head
    global tail
    n = len(A)
    hm = {}
    for i in range(n):
        if A[i] in hm:
            ref = hm[A[i]]
            deleteByRef(ref)
            count -=1
        else:
            if count == capacity:
                del hm[head.value]
                deleteFromFront()
                count -=1
        insertAtEnd(A[i])
        hm[A[i]] = tail
        count +=1
    printAll(head)
        
A=[7,9,3,2,10,12,3,2,10,7,9,11]


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
            
    
head = None


def generateLinkedList(A):
    global head
    n = len(A)
    head = Node(A[0])
    temp = head
    for i in range(1,n):
        n = Node(A[i])
        temp.next = n
        temp = n
        
def getMid(head):
    fast = head
    slow = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head):
    current = head
    prev = None
    while current != None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
        
def isPalindrome(head):
    mid = getMid(head)
    h2 = mid.next
    mid.next = None
    h2 = reverse(h2)
    p1 = head
    p2 = h2
    
    while p1 != None and p2 != None:
        if p1.value != p2.value :
            return False
        p1 = p1.next
        p2 = p2.next
    return True
    
        

A=["racecar", "level", "apple", "deified", "banana", "kayak", "programming", "radar", "civic", "computer"]

for i in range(len(A)):
    generateLinkedList(A[i])
    print(A[i],isPalindrome(head))






