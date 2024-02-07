def findIndex(A,k):
    n = len(A)
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r) // 2
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    return -1

A=[3,5,7,11,13,16,18,27]
k = 27

def findFirstIndex(A,k):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l+r) // 2
        if (A[mid] == k and mid == 0) or (A[mid] == k and A[mid - 1] != k):
            return mid
        elif A[mid] >= k:
            r = mid - 1
        else:
            l = mid + 1
    return - 1

A=[3,5,7,7,7,7,7,8,8,8,8,9,9,10,10]
k = 7

def findLastIndex(A,k):
    n = len(A)
    l = 0
    r = n-1
    
    while l <= r:
        mid = (l+r) // 2
        if ( A[mid] == k  and  mid == n- 1) or (A[mid] == k and A[mid+1] != k):
            return mid
        elif A[mid] <= k:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def findPeakElement(A):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l+r) // 2
        if (mid == 0 and A[mid] > A[mid + 1]) or (mid == n-1 and A[mid] > A[mid-1])  or (A[mid] > A[mid-1] and A[mid] > A[mid+1] ):
            return A[mid]
        elif A[mid] < A[mid+1]:
            l = mid + 1
        else:
            r = mid - 1
    return -1
    
A=[1,2,3,4,5]

def findNonRepeatingElement(A):
    n = len(A)
    l = 0
    r = n - 1
    while l<=r:
        mid = (l+r) // 2
        if (mid == 0 and A[mid] != A[mid+1])or mid == n-1 and A[mid] != A[mid-1] or A[mid] != A[mid-1] and A[mid] != A[mid+1]:
            return A[mid]
        elif (mid % 2 == 0 and A[mid] == A[mid+1]) or mid % 2 != 0 and A[mid] == A[mid-1]:
            l=mid + 1
        else:
            r = mid - 1
    
A=[3,3,5,5,9,9,10,10,12,12,15]

print(findNonRepeatingElement(A))