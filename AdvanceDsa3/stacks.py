class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def push(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count +=1
    
    def top(self):
        if self.head == None:
            return self.head
        return self.head.value
    
    def isEmpty(self):
        if self.count == 0:
            return True
        return False
    
    def pop(self):
        if self.head == None:
            print("Stack is empty")
        else:
            self.head = self.head.next
        self.count -=1
    
    def printAll(self):
        ans = []
        temp = self.head
        while temp != None:
            ans.append(temp.value)
            temp = temp.next
        print(ans)

l = SinglyLinkedList()

def isOpening(s):
    l = ['(','{','[']
    if s in l:
        return True
    return False

def isMatching(opening,closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False

def validParentheses(A):
    n = len(A)
    stack = []
    for i in range(n):
        if isOpening(A[i]):
            stack.append(A[i])
        else:
            if len(stack) > 0:
                top = stack[-1]
                stack.pop()
                if isMatching(top,A[i]) == False:
                    return False
            else:
                return False
    if len(stack) == 0:
        return True
    return False
                    
    
A='()([])'
        
def removeConsecutive(A):
    n = len(A)
    stack = []
    for i in range(n):
        if len(stack) == 0:
            stack.append(A[i])
        else:
            top = stack[-1]
            if top == A[i]:
                stack.pop()
            else:
                stack.append(A[i])
    print(stack)
        
    
A='abbbccca'

def calculate(num1,num2,op):
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        return num1 + num2
    if op == '-':
        return  num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 / num2
    

def isOperator(s):
    l = ['+','-', '*', '/']
    if s in l:
        return True
    return False

def postfixExpression(A):
    n = len(A)
    stack = []
    for i in range(n):
        if isOperator(A[i]):
            num2 = stack[-1]
            stack.pop()
            num1 = stack[-1]
            stack.pop()
            calculated_value = calculate(num1, num2,A[i])
            stack.append(calculated_value)
        else:
            stack.append(A[i])
    print(stack)
    
A='35+2-25*-'

postfixExpression(A)
