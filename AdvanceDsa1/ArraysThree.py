def find(A,k):
    n = len(A)
    m = len(A[0])
    i = 0
    j = m - 1
    while i < n and j >= 0:
        if A[i][j] == k:
            return True
        if A[i][j] < k:
            i+=1
        else:
            j-=1
    return False


matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]
k=100

A=[[1,3],[2,6],[8,10],[15,18]]

def mergeOverlappingIntervals(A):
    n = len(A)
    current_interval = A[0]
    ans = []
    for i in range(1,n):
        current_interval_start_time = current_interval[0]
        current_interval_end_time = current_interval[1]
        next_interval_start_time = A[i][0]
        next_interval_end_time = A[i][1]
        if current_interval_end_time > next_interval_start_time:
            start_time = min(current_interval_start_time,next_interval_start_time)
            end_time = max(current_interval_end_time,next_interval_end_time)
            new_interval = [start_time,end_time]
            ans.append(new_interval)
            current_interval_start_time = start_time
            current_interval_end_time = end_time
        else:
            ans.append(A[i])
    return ans
    
mergeOverlappingIntervals(A)
