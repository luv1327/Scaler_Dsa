

def maxSubArrSum(A):
    n = len(A)
    ans = 0
    max_ans = float('-inf')
    for i in range(n):
        ans += A[i]
        max_ans = max(max_ans,ans)
        if ans < 0:
            ans = 0
    return max_ans
            
            
    
A=[-3,7,2,-6,-4,-2,8,-9]


def findFirstPositive(A):
    n = len(A)
    for i in range(1,n):
        flag = 0
        for j in range(n):
            if A[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    return n+1
        
A=[-2,4,6,-1,9,1,10,2,3]


def findBySort(A):
    A.sort()
    start = False
    n = len(A)
    j = 1
    for i in range(n):
        if A[i] > 0:
            start = True
        if start:
            if A[i] == j:
                j+=1
            else:
                return j
    return n+1
            



def findWithHashMap(A):
    n = len(A)
    hm = {}
    for i in range(n):
        if A[i] in hm:
            hm[A[i]] +=1
        else:
            hm[A[i]] = 1
    for i in range(1,n):
        if i not in hm:
            return i
    return n+1
            


def findFirstMissing(A):
    n = len(A)
    for i in range(n):
        while A[i] != i+1 and A[i] > 0 and A[i] <= n:
            target_idx = A[i] - 1
            if A[i] == A[target_idx]:
                break
            A[target_idx],A[i] = A[i],A[target_idx]
    for i in range(n):
        if A[i] != i+1:
            return i+1
    return n+1
A=[1,1]  


def trappingRainWater(A):
    n = len(A)
    pf_left = [0] * n
    pf_right = [0] * n
    pf_left[0] = A[0]
    pf_right[n-1] = A[n-1]
    for i in range(1,n):
        pf_left[i] = max(pf_left[i-1],A[i])
    for i in range(n-2,-1,-1):
        pf_right[i] = max(pf_right[i+1],A[i])
    trapped_water = 0
    for i in range(1,n-1):
        trapped = min(pf_left[i-1],pf_right[i+1]) - A[i]
        if trapped > 0:
            trapped_water +=trapped
    return trapped_water
    
A=[0,1,0,2,1,0,1,3,2,1,2,1]




