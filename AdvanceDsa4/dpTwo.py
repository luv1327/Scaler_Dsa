A=[2,-1,-4,5,3,-1,4,7]
n=len(A)
dp = [None] * (n+1)
def houseRobbery(i):
    if i < 0:
        return 0
    if dp[i] != None:
        return dp[i]
    t = A[i] + houseRobbery(i-2)
    dt = houseRobbery(i-1)
    dp[i] =  max(t,dt)
    return dp[i]
    
def houseRobberyTopDown(A):
    n = len(A)
    dp = [None] * n
    dp[0] = A[0]
    dp[1] = max(A[0],A[1])
    for i in range(2,n):
        dp[i] = max(A[i] + dp[i-2],dp[i-1])
    return dp[n-1]