def findLeft(A):
    n = len(A)
    stack = []
    ans = []
    for i in range(n):
        while len(stack) > 0 and A[i] <= stack[-1]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            top = stack[-1]
            if A[i] > top:
                ans.append(top)
        stack.append(A[i])
    return ans
            
def findLeftIndex(A):
    n = len(A)
    stack = []
    ans = []
    for i in range(n):
        while len(stack) > 0 and A[i] <= A[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            ans.append(0 )
        else:
            top = A[stack[-1]]
            if A[i] >  top:
                ans.append(stack[-1] + 1)
        stack.append(i)
    return ans

def findRightIndex(A):
    n = len(A)
    stack = []
    ans = [0] * n
    for i in range(n-1,-1,-1):
        while len(stack) > 0 and A[i]<= A[stack[-1]]:
            stack.pop()
        
        if len(stack) == 0:
            ans[i] = n - 1
        else:
            top = A[stack[-1]]
            if A[i] > top:
                ans[i] = stack[-1] - 1
        stack.append(i)
    return ans
        
    
A=[5,3,7,11,9,12,8,6]
B=[13,6,10,12,11,18,19,17,9]

def findMaxRectangleHistogram(A):
    n = len(A)
    left = findLeftIndex(A)
    right = findRightIndex(A)
    max_rectangle = float('-inf')
    for i in range(n):
        current_rectangle = (right[i] - left[i])+ 1
        current_rectangle *= A[i]
        max_rectangle = max(max_rectangle, current_rectangle)
    return max_rectangle
    
    
A=[2,1,3,5,4,3,4,6]


    