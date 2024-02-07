def minSwaps(A,B):
    n = len(A)
    k = 0
    for i in range(n):
        if A[i] < B:
            k+=1
    
    min_swaps = 0
    
    for i in range(k):
        if A[i] > B:
            min_swaps +=1
    l = 1
    r = k
    ans = min_swaps
    while r < n:
        if A[l-1] < B and A[r] > B:
            min_swaps+=1
        if A[l-1] > B and A[r] < B:
            min_swaps -=1
        ans = min(min_swaps,ans)
        l+=1
        r+=1
        
    return ans
        
A=[1,10,12,14,3,5,11,13]
B=8  
print(minSwaps(A,B))