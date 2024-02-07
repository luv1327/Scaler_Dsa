import math

n = 6
dp =[None] * (n+1)

def fib(n):
    if n <= 1:
        return n
    if dp[n] != None:
        return dp[n]
    dp[n] = fib(n-2) + fib(n-1)
    return dp[n]

dp = [None] * (n+1)
def bottomUpFib(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = 4
dp = [None] * (n+2)
def totalNoOfWaysStair(n):
    if n <= 1:
        return n
    if dp[n] != None:
        return dp[n]
    
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
    
n=500
dp=[None] * (n+1)
def minNumberOfSqaure(n):
    if n <= 0:
        return 0
    if dp[n] != None:
        return dp[n]
    min_count = float('+inf')
    for i in range(1,int(math.sqrt(n))+1):
        x = 1+minNumberOfSqaure(n - i** 2)
        min_count = min(x,min_count)
    dp[n] = min_count
    return dp[n]
    
print(minNumberOfSqaure(500))
n= 500
dp = [0] * (n+1)
def minNumberOfSqaureBottomUp(n):
    dp[0] = 0
    for i in range(1,n+1):
        min_val = float('+inf')
        for j in range(1,int(math.sqrt(i))+1):
            val = 1 + dp[i- j ** 2]
            min_val = min(min_val,val)
        dp[i] = min_val
    return dp[n]
        
print(minNumberOfSqaureBottomUp(n))
    

    