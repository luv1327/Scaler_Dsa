def searchInRotatedSortedArr(A):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l+r) // 2
        if (mid == 0 and A[mid] > A[mid+1]) or (mid == n-1 and A[mid] > A[mid-1] ) or A[mid] > A[mid+1] and A[mid] > A[mid-1]:
            return A[mid]
        elif A[mid] > A[0]:
            l = mid + 1
        else:
            r = mid - 1
            

A=[9,11,12,13,14,1,2,3]
print(searchInRotatedSortedArr(A))