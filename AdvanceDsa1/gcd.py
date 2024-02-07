def gcdBruteForceIterative(a,b):
    for i in range(min(a,b),-1,-1):
        if a % i == 0 and b % i == 0:
            return i
        
def gcdRecursive(a,b):
    if b == 0:
        return a
    if a < b:
        a,b=b,a
    return gcdRecursive(a-b,b)
a=15
b=35   

def gcdOptimised(a,b):
    if b == 0:
        return a
    return gcdOptimised(b,a % b)


def gcdArr(A):
    n = len(A)
    ans = 0
    for i in range(n):
        ans = gcdOptimised(ans,A[i])
    return ans
    
A=[6,12,15]

print(gcdArr(A))