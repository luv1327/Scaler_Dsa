def isWorking(A,k,time):
    n = len(A)
    w = 1
    temp_time = 0
    for i in range(n):
        temp_time += A[i]
        if temp_time > time:
            w+=1
            temp_time = A[i]
    if w <= k:
        return True
    return False
        

def minTime(A,k):
    n = len(A)
    l = max(A)
    r = sum(A)
    min_time = float('+inf')
    while l <= r:
        mid = (l+r) // 2
        if isWorking(A,k,mid):
            min_time = min(min_time,mid)
            r = mid - 1
        else:
            l = mid + 1
    return min_time
    
A= [3,5,1,7,8,2,5,3,10,1,4,7,5,4,6]
k = 3

def canPlace(A,cows,distance):
    n = len(A)
    cow_count = 1
    last_placed = A[0]
    for i in range(1,n):
        if A[i] - last_placed >= distance:
            last_placed = A[i]
            cow_count +=1
    
    if cow_count >= cows:
        return True
    return False
            
def placeCows(A,cows):
    n = len(A)
    l = 0
    r = A[n-1]
    max_distance = float('-inf')
    while l <= r:
        mid = (l+r) // 2
        if canPlace(A,cows,mid):
            max_distance = max(max_distance,mid)
            l = mid + 1
        else:
            r = mid - 1
    
    return max_distance
            
      
A=[2,6,11,14,19,25,30,39,43]
cows = 4

print(placeCows(A,cows))