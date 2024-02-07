class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        
import linkedListTwo
        
    
def canEliminateBoringSubstring(A):
    n = len(A)
    s1 = set()
    s2 = set()
    for i in range(n):
        num = ord(A[i])
        if num % 2 != 0:
            s1.add(A[i])
        else:
            s2.add(A[i])
    for x in s1:
        target_idx = ord(x) + 3
        for i in range(target_idx,ord('z') + 1,2):
            if chr(i) in s2:
                return True
    return False
            
        
        
def cloneLinkedListWithRandomPointer(head):
    h2 = ListNode(0)
    t1 = head
    t2 = h2
    while t1 != None:
        t2.next = ListNode(t1.data)
        t1 = t1.next
        t2 = t2.next
    hm = {}
    t1 = head
    t2 = h2
    while t1 != None:
        hm[t1] = t2
        t1 = t1.next
        t2 = t2.next
    t1 = head
    while t1 != None:
        random_pointer = t1.random
        p1 = hm[t1]
        if random_pointer != None: 
            target = hm[random_pointer]
        p1.random = target
        t1 = t1.next
    return h2.next
        
    

       
        
# A=[2, 6,7, 12, 15, 20] 
# head = ListNode(10)
# linkedListTwo.generateLinkedList(head,A) 
# cloneLinkedListWithRandomPointer(head)

def countPairBruteForce(A,k):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for x in range(j+1,n):
                if A[i] + A[j] + A[x] == k:
                    count +=1
    return count

def countPair(A,k):
    A.sort()
    n = len(A)
    s = set()
    for i in range(n):
        left = i+1
        right = n - 1
        while left < right:
            current_sum = A[i] + A[left] + A[right]
            if current_sum == k:
                s.add((A[i],A[left],A[right]))
                left +=1
                right -=1
            if current_sum < k:
                left+=1
            else:
                right -=1
    output = []
    for triplets in s:
        output.append(triplets)
    return output
        
        
        
             
            

A=[-1,0,1,2,-1,-4]

print(countPair(A,0))

