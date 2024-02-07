def findK(A,k):
    n = len(A)
    l = 0
    r = n - 1
    while l < r:
        value = A[l] + A[r]
        if value == k:
            return True
        elif value < k:
            l+=1
        else:
            r-=1
    return False

A=[-3,0,1,3,6,8,11,14,18,25]
k=17

def findCountOfK(A,k):
    n = len(A)
    hm = {}
    for i in range(n):
        if A[i] in hm:
            hm[A[i]] +=1
        else:
            hm[A[i]] = 1
    s = set()
    for i in range(n):
        s.add(A[i])
    arr = []
    for x in s:
        arr.append(x)
    l = 0
    r = len(arr) - 1
    count = 0
    arr.sort()
    print(arr)
    while l <= r:
        if arr[l] + arr[r] == k:
            if arr[l] == arr[r]:
                val = hm[arr[l]]
                count += val * (val - 1) // 2
            else:
                count += hm[arr[l]] * hm[arr[r]]
            l+=1
            r-=1    
        elif arr[l] + arr[r] > k:
            r-=1
        else:
            l+=1
    return count
    
A=[0,0,0,2,2,2,2,2,4,4,10,10,]
k = 4

def checkK(A,k):
    n = len(A)
    i = 0
    j = 1
    while j < n:
        if A[j] - A[i] == k:
            return True
        elif A[j] - A[i] < k:
            j+=1
        else:
            i+=1
    return False 
            

A=[-3,0,1,3,6,8,11,14,18,25]
k = 5

def maxWater(A):
    n = len(A)
    l = 0
    r = n - 1
    max_water = float('-inf')
    while l < r :
        current_water_stored = min(A[l],A[r]) * (r - l)
        max_water = max(max_water,current_water_stored)
        if A[r] > A[l]:
            l+=1
        else:
            r -=1
    return max_water
    
A=[3,7,4,5,2]

print(maxWater(A))