def checkBit(n,i):
    if (n >> i & 1) == 1:
        return True
    return False

def subsequenceSum(A,k):
    n = 2 ** len(A)
    for i in range(n):
        current_sum = 0
        for j in range(len(A)):
            if checkBit(i,j):
                current_sum += A[j]
        if current_sum == k:
            return True
    return False
                
    
A=[1,2,3] 

def findAllSubsetsSumBruteForce(A):
    n = 2 ** len(A) 
    ans = []
    for i in range(n):
        curr_sum = 0
        for j in range(len(A)):
            if checkBit(i,j):
                curr_sum += A[j]
        ans.append(curr_sum)
    return sum(ans)
    
def findAllSubsetsSumOptimised(A):
    n = len(A)
    mul = 2 ** (n-1)
    ans = 0
    for i in range(n):
        ans += mul * A[i]
    return ans // 2

def solve(A):
    return sum(A) // 2
        
    


print(solve(A))
                