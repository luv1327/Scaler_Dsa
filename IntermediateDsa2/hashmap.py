def getCount(A,Q):
    n = len(A)
    hm = {}
    for i in range(n):
        if A[i] in hm:
            hm[A[i]] +=1
        else:
            hm[A[i]] = 1
            
    for x in Q:
        if x in hm:
            print(x,hm[x])
        else:
            print(x,0)


A=[2,6,3,8,2,8,2,3,8,10,6]
Q=[6,8,2]

def findFirstNonRepeating(A):
    hm = {}
    n = len(A)
    for i in range(n):
        if A[i] in hm:
            hm[A[i]] +=1
        else:
            hm[A[i]] = 1
            
    for i in range(n):
        if hm[A[i]] == 1:
            return A[i]
        
def findDistinctElements(A):
    n = len(A)
    s = set()
    for i in range(n):
        s.add(A[i])
    return len(s)

            
def findSubArraySumZero(A):
    n = len(A)
    pf = [0] * n
    pf[0] = A[0]
    hm={}
    for i in range(n):
        pf[i] = pf[i-1] + A[i]
    for i in range(n):
        if pf[i] == 0:
            return True
        if pf[i] in hm:
            hm[pf[i]] +=1
        else:
            hm[pf[i]] = 1
    
    for i in range(n):
        if hm[pf[i]] >= 2:
            return True
    return False
    
A=[3,3]

print(findSubArraySumZero(A))