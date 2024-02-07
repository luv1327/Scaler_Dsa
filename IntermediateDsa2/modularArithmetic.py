def findPow(a,n,p):
    res = 1
    for i in range(n):
        res = (res * a) % p
    return res 

def findNumP(A,p):
    res = 0
    n = len(A)
    for i in range(n):
        res += (A[i] % p  *  findPow(10,n-i-1,p)) % p
    
    return res
    
A=[8,9,3,2,6,4,1,9]

print(findNumP(A,8))