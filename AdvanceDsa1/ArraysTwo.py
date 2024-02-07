def findSubMatSum(A):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            print(A[i][j],i,j)




def generatePf(A):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(1,m):
            A[i][j] =A[i][j] +  A[i][j-1]
    
    for j in range(m):
        for i in range(1,n):
            A[i][j] = A[i][j] + A[i-1][j]

def findQ(A,Q):
    generatePf(A)
    n = len(Q)
    for i in range(n):
        cs = Q[i][0]
        rs = Q[i][1]
        re = Q[i][2]
        ce = Q[i][3]
        
        total_ans = A[re][ce]
        if cs > 0:
            total_ans -= A[re][cs-1]
        if rs > 0: 
            total_ans -= A[rs-1][ce]
        if cs > 0 and rs > 0:
            total_ans += A[rs-1][cs-1]
        print(total_ans)

Q=[
    [1,1,2,2],
    [0,0,1,2]
]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def sumOfAllSubMatrixSum(A):
    n = len(A)
    m= len(A[0])
    total_sum = 0
    for i in range(n):
        for j in range(m):
            top_right_count  =  (i+1) * (j+1)
            bottom_right_count = (n - i) * (m - j)
            total_count = top_right_count * bottom_right_count
            total_sum += A[i][j]  * total_count
    return total_sum
    

def maxSubMatrixSum(A):
    n = len(A)
    m = len(A[0])
    for j in range(m):
        for i in range(1,n):
            A[i][j] = A[i][j] + A[i-1][j]
    max_sum = float('-inf')
    curr_sum = 0
    i = n - 1
    for j in range(m):
        curr_sum += A[i][j]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum
        
    
matrix = [
    [-3,2,3,4,-6,4,5],
    [5,5,-5,2,2,-7,-6],
    [-4,-3,1,-1,1,4,1]
]

print(maxSubMatrixSum(matrix))