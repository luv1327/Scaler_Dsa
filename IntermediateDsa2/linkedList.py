import random

start = 10
end = 100

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    
    
head = Node(random.randint(start,end))

def generateLinkedList(head):
    temp = head
    for i in range(10):
        n = Node(random.randint(start,end))
        temp.next = n
        temp = temp.next

generateLinkedList(head)
        
def printLl(head):
    temp = head
    arr= []
    while temp != None:
        arr.append(temp.data)
        temp = temp.next
    print(arr)

def insertAtHead(val):
    global head
    new_node = Node(val)
    new_node.next = head
    head = new_node
    
def insertAtEnd(val):
    global head
    if head == None:
        head = Node(val)
    else:
        temp = head
        while temp and temp.next != None:
            temp = temp.next
        temp.next = Node(val)
    
def createALinkedList(n):
    head = Node(1)
    tail = head
    for i in range(2,n+1):
        tail.next = Node(i)
        tail = tail.next
    return head
    
h = createALinkedList(10)


def insertAtKth(val,k):
    global head
    new_node = Node(val)
    temp = head
    printLl(head)
    for i in range(k-1):
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node

    
# insertAtKth(76,0)

printLl(head)

def printInReverse(head):
    if head == None:
        return
    printInReverse(head.next)
    print(head.data)

printLl(head)
printInReverse(head)