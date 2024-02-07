def prefixSum(A,Q):
    n = len(A)
    pf = []
    pf.append(A[0])
    for i in range(1,n):
        pf.append(pf[i-1] + A[i])
    for i in range(len(Q)):
        l = Q[i][0]
        r = Q[i][1]
        if l == 0:
            print(pf[r])
        else:
            print(pf[r] - pf[l-1])
    
    
A=[3,2,-1,5,2]
Q=[
    [0,2],
    [1,3]
]


def findPf(A):
    n = len(A)
    pf = [0] * (n)
    pf[0] = A[0]
    for i in range(1,n):
        pf[i] = pf[i-1] + A[i]
    return pf
    

def equilibrium(A):
    n = len(A)
    pf = findPf(A)
    count = 0
    for i in range(n):
        left_sum = 0
        right_sum = 0
        if i != 0:
            left_sum = pf[i-1]
        if i != n-1:
            right_sum = pf[n-1] - pf[i]
        
        if left_sum == right_sum:
            count +=1
    return count

A=[-3,2,4,-1]

def pfEven(A):
    n = len(A)
    pf = [0] * n
    pf[0] = A[0]
    for i in range(1,n):
        if i % 2 == 0:
            pf[i] = pf[i-1] + A[i]
        else:
            pf[i] = pf[i-1]
    
def pfOdd(A):
    n = len(A)
    pf = [0] * n
    for i in range(1,n):
        if i % 2 != 0:
            pf[i] = pf[i-1] + A[i]
        else:
            pf[i] = pf[i-1]
    print(pf)
        
    
    
A=[2,3,4,2,-1,3,5]

pfOdd(A)