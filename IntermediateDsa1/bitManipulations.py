def findSingleElement(A):
    n = len(A)
    ans = 0
    for i in range(n):
        ans ^= A[i]
    return ans
A=[2,2,3,4,3,7,3,3,7,4,6]

print(findSingleElement(A))