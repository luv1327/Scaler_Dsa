def printInClockwise(A):
    n = len(A)
    m = len(A[0])
    ans = []
    row = 0
    col = 0
    range_can = 0
    if len(A) % 2 == 0 or len(A[0]) % 2 == 0 :
        range_can = 1
    else:
        range_can = 2
    while n >=1:
        for i in range(m-1):
            ans.append(A[row][col])
            col+=1
        for i in range(n-1):
            ans.append(A[row][col])
            row+=1
        
        for i in range(m-1):
            ans.append(A[row][col])
            col-=1
        
        for i in range(n-1):
            ans.append(A[row][col])
            row-=1
        m-=2
        n-=2
        row+=1
        col+=1
    if n == 1:
        ans.append(A[row][col])
    return ans
        
            

A=[[6,9,7]]

def maxSubArraySumOfK(A,k):
    n = len(A)
    ans = float('-inf')
    curr_sum = 0
    for i in range(k):
        curr_sum += A[i]
    ans = max(ans,curr_sum)
    l = 1
    r = k 
    while r < n:
        curr_sum-= A[l-1]
        curr_sum += A[r]
        ans = max(ans,curr_sum)
        l+=1
        r+=1
    return ans
        

A=[5,3,-2,1,6,2,-1,4,3]
print(maxSubArraySumOfK(A,4))