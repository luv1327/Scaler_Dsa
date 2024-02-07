def findGreater(A):
    n = len(A)
    max_element = A[0]
    for i in range(1,n):
        max_element = max(max_element,A[i])
    max_count = 0
    for i in range(n):
        if max_element == A[i]:
            max_count +=1
    return len(A) - max_count
            
def twoSum(A,k):
    n = len(A)
    for i in range(n):
        for j in range(1,n):
            if A[i] + A[j] == k:
                return True
    return False  

def swap(A,i,j):
    A[i],A[j] = A[j],A[i]
def reverseArr(A):
    n = len(A)
    l = 0
    r = n - 1
    while l < r:
        swap(A,l,r)
        l+=1
        r-=1      
    return A


def reversePart(A,l,r):
    while l < r:
        swap(A,l,r)
        l+=1
        r-=1
    return A

def reverseKTimes(A,k):
    n = len(A)
    reversePart(A,0,n-1)
    reversePart(A,0,k-1)
    reversePart(A,k,n-1)
    return A


A=[3,-2,1,4,6,9,8]
k=3

print(A)







