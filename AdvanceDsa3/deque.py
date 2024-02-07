from collections import deque

def findMaxInWindowBF(A,k):
    n = len(A)
    ans = []
    for i in range(n):
        cur_max = float('-inf')
        if i + k <= n:
            for j in range(i,i+k):
                cur_max = max(cur_max,A[j])
            ans.append(cur_max)
    return ans


A=[5,6,5,7,8,9,7,3,2,5,8]
k=4

def findMaxInWindow(A,k):
    n = len(A)
    dq = deque()
    ans = []
    for i in range(k):
        while len(dq) > 0 and A[i] > A[dq[-1]]:
            dq.pop()
        dq.append(i)
    ans.append(A[dq[0]])
    l = 1
    r = k
    while r < n:
        if len(dq) > 0 and  l-1 == dq[0]:
            dq.popleft()
        while len(dq) > 0 and A[r] > A[dq[-1]]:
            dq.pop()
        dq.append(r)
        ans.append(A[dq[0]])
        l+=1
        r+=1
    return ans
        
    
def findFirstNonRepeating(A):
    n = len(A)
    hm = {}
    dq = deque()
    ans = []
    for i in range(n):
        if A[i] in hm:
            hm[A[i]] +=1
        else:
            hm[A[i]] = 1
        if hm[A[i]] == 1:
            dq.append(A[i])
        
        while len(dq) > 0 and hm[dq[0]] > 1:
            dq.popleft()
        
        if len(dq) > 0:
            ans.append(dq[0])
        else:
            ans.append('#')
    return ans
        

A='abba'

findFirstNonRepeating(A)
