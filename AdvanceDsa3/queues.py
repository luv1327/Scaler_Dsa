from collections import deque

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.back = None
#         self.count = 0
    
#     def enque(self,data):
#         new_node = Node(data)
#         if self.front == None and self.back == None:
#             self.front = new_node
#             self.back = new_node
#         else:
#             self.back.next = new_node
#             self.back = new_node
#         self.count +=1
    
#     def deque(self):
#         if self.front == None and self.back == None:
#             print('Queue is empty')
#         elif self.count == 1:
#             self.front = None
#             self.back = None
#         else:
#             self.front = self.front.next
#         self.count -=1 
    
#     def isEmpty(self):
#         if self.count == 0:
#             return True
#         return False 
    
#     def getFront(self):
#         if self.front == None:
#             return None
#         return self.front.data 
    
#     def getBack(self):
#         if self.back == None:
#             return None
#         return self.back.data       
    
#     def printAll(self):
#         ans = []
#         temp = self.front
#         while temp != None:
#             ans.append(temp.data)
#             temp = temp.next
#         print(ans)

# q = Queue()

# q.enque(10)
# q.enque(20)
# q.enque(30)
# q.deque()
# q.enque(100)
# q.printAll()

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def move(self):
        while len(self.s1) > 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
    
    def deque(self):
        if len(self.s2) == 0:
            self.move()
        if len(self.s2) > 0:
            self.s2.pop()
    
    def enque(self,data):
        self.s1.append(data)
        
def findNthNumber(n):
    q = deque()
    q.append(1)
    q.append(2)
    c = 0
    while c < n:
        front = q[0]
        q.popleft() 
        c+=1 
        if c == n:
            return front
        v1 = (front * 10) + 1
        v2 = (front * 10) + 2
        q.append(v1)
        q.append(v2)
        
def findNthNumberPalindrome(n):
    q = deque()
    q.append(1)
    q.append(2)
    c = 0
    while c < n:
        front = q[0]
        q.popleft() 
        c+=1 
        if c == n:
            s = str(front)
            rs = s[::-1]
            ans = s + rs
            return  ans
        v1 = (front * 10) + 1
        v2 = (front * 10) + 2
        q.append(v1)
        q.append(v2)
    
print(findNthNumberPalindrome(2))
            
    


