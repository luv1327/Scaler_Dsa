import heapq

def getFirstKMinElements(A,k):
    n = len(A)
    max_heap = []
    for i in range(k):
        heapq.heappush(max_heap,-A[i])
    r = k
    while r < n:
        current_max = -max_heap[0]
        if A[r] > current_max:
            pass
        else:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap,-A[r])
        r+=1
        

def getMedianNum(A):
    n = len(A)
    mid = n // 2
    if n % 2 != 0:
        return A[mid]
    else:
        val = A[mid-1] + A[mid] 
        return val / 2
    

def runningMedian(A):
    n = len(A)
    left = []
    right = []
    median = []
    heapq.heappush(left,-A[0])
    median.append(A[0])
    for i in range(1,n):
        val = -left[0]
        if A[i] > val:
            heapq.heappush(right,A[i])
        else:
            heapq.heappush(left,-A[i])
        
        if len(left) < len(right):
            heapq.heappush(left,-right[0])
            heapq.heappop(right)
        elif len(left) - len(right) > 1:
            heapq.heappush(right,-left[0])
            heapq.heappop(right)
        if len(left) == len(right):
            val1 = -left[0]
            val2 = right[0]
            val3 = (val1 + val2) / 2
            median.append(val3) 
        else:
            val = -left[0]
            median.append(val)
    return median


def sortMatrix(A):
    n = len(A)
    m = len(A[0])
    sorted_arr = []
    h = []
    for col in range(0,1):
        for row in range(n):
            val = (A[row][col],row,col)
            heapq.heappush(h,val)
            
    while len(h) > 0:
        get_min = h[0]
        heapq.heappop(h)
        val = get_min[0]
        sorted_arr.append(val)
        i = get_min[1]
        j = get_min[2]
        if j < m - 1:
            j +=1
            heapq.heappush(h,(A[i][j],i,j))
    print(sorted_arr)
            
            
        
        
    
    
A=[
    [1,3,5,7],
    [2,4,6,8],
    [5,7,9,10],
    [4,5,6,7]
]

sortMatrix(A)
    
            
        

A=[4,9,6,2,1,10,9,7,3,5]

runningMedian(A)