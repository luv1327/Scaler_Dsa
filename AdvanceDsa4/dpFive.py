A=[2,3,8,1,3]
n = len(A)

def lis():
    n = len(A)
    dp = [1] * n
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if A[i] > A[j]:
                dp[i] = max(dp[i],dp[j] + 1)
    return max(dp)
    
    
    
A=[3,5,2,1,4,5,2]
def stocks():
    n = len(A)
    max_profit = float('-inf')
    purchase = A[0]
    for i in range(n):
        profit = A[i] - purchase
        max_profit = max(max_profit,profit)
        purchase = min(purchase,A[i])
    print(max_profit)
    
stocks()