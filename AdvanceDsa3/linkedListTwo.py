import random
import linkedListWithLoop

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
def printAll(head):
    ans = []
    temp = head
    while temp != None:
        ans.append(temp.data)
        temp = temp.next
    print(ans)


def generateLinkedList(head,A):
    temp = head
    for i in A:
        n = Node(i)
        temp.next = n
        temp = n
        

def getKthElement(head,k):
    temp = head
    while k > 0 and temp != None:
        temp = temp.next
        k-=1
    return temp

def size(head):
    temp = head
    count = 0
    while temp != None:
        count +=1
        temp = temp.next
    return count

def getMiddle(head):
    count = size(head)
    if count % 2 != 0:
        return getKthElement(head,count // 2)
    return getKthElement(head,(count // 2)-1)

def getMiddleByTurtleAndHareAlgo(head):
    if head == None:
        return head
    fast = head
    slow = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


h1 = Node(0)
h2 = Node(0)
A=[2, 6,7, 12, 15, 20]
B=[4, 8, 10,13,80]
generateLinkedList(h1,A)
generateLinkedList(h2,B)

def merge(h1,h2):
    if h1 == None:
        return h2
    elif h2 == None:
        return h1
    h3 = Node(0)
    temp = h3
    while h1 != None and h2 != None:
        if h1.data <= h2.data:
            temp.next = h1
            temp = temp.next
            h1 = h1.next
        else:
            temp.next = h2
            temp = temp.next
            h2 = h2.next
    if h1 == None:
        temp.next = h2
    if h2 == None:
        temp.next = h1
    return h3.next
        
    
A=[56, 10, 27, 84, 72, 90, 50, 15, 93, 1]
head = Node(random.randint(0,100))
generateLinkedList(head,A)
def mergeSort(head):
    # head.next means there is one element
    if head.next == None:
        return head
    mid = getMiddleByTurtleAndHareAlgo(head) 
    h2 = mid.next
    mid.next = None
    x1 = mergeSort(head)
    x2 = mergeSort(h2)
    return merge(x1,x2)
# printAll(head)  
# head = mergeSort(head)
# printAll(head)
length = 10
loop_index = 3
head = linkedListWithLoop.create_linked_list_with_loop(length, loop_index)


def detectLoop(head):
    fast = head
    slow = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def findLoopPoint(head):
    fast = head
    slow = head
    loop_node = None
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            loop_node = slow
            break
    s1 = head
    while s1 != loop_node:
        s1 = s1.next
        loop_node = loop_node.next
    return s1

def breakLoop(head):
    fast = head
    slow = head
    loop_node = None
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            loop_node = slow
            break
    s1 = head
    while s1.next != loop_node.next:
        s1 = s1.next
        loop_node = loop_node.next
    loop_node.next = None
    # printAll(head)
    
breakLoop(head)
    
            


