def twoSum(A,k):
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            if A[i] + A[j] == k:
                print(i,j)
                return True
A=[0,10,20]
k=0


def twoSumOptimised(A,B):
    n = len(A)
    hm = {}
    for i in range(n):
        k = B - A[i]
        if k in hm:
            print(k,A[i])
            return True
        hm[A[i]] = i
    return False
        
def findDistinctInKSubArr(A,k):
    n = len(A)
    hm={}
    for i in range(k):
        if A[i] in hm:
            hm[A[i]] +=1
        else:
            hm[A[i]] = 1
    ans = []
    ans.append(len(hm))
    l = 1
    r = k
    while r < n:
        expiring = A[l-1]
        incoming = A[r]
        hm[expiring] -=1
        if hm[expiring] == 0:
            del hm[expiring]
        if incoming in hm:
            hm[incoming] +=1
        else:
            hm[incoming] = 1
        ans.append(len(hm))
        l+=1
        r+=1
    return ans
    
A=[2,4,3,8,3,9,4,9,4,10]
k=4
findDistinctInKSubArr(A,k)
    
        
        