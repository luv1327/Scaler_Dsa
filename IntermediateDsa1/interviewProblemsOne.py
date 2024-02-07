import math

def findMaxConsecutiveOne(A):
    n = len(A)
    max_length = float('-inf')
    for i in range(n):
        if A[i] == 0:
            l = i - 1
            r = i+1
            while l >= 0 and A[l] == 1:
                l-=1
            while r < n and A[r] == 1:
                r+=1
            l+=1
            r-=1
            max_length = max(max_length,r-l+1)
    return max_length
    
A=[1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1]

def findTriplets(A):
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if A[i] < A[j] and A[j] < A[k]:
                    count +=1
    return count
        
  
def findTripletsOptimised(A):
    n = len(A)
    ans = 0
    for i in range(n):
        left_count = 0
        for j in range(i-1,-1,-1):
            if A[i] > A[j]:
                left_count +=1
        right_count = 0
        for j in range(i+1,n):
            if A[i] < A[j]:
                right_count +=1
        ans += left_count * right_count
    return ans
                
    
A=[2,6,9,4,10]

def findClosestPow(n):
    for i in range(n):
        if 2 ** (i+1) > n:
            return 2 ** i

def josephus(n):
    closest_power = findClosestPow(n)
    kills = n - closest_power
    winner = (2 * kills) + 1
    return winner

n = 66


