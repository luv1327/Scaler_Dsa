def findPairBruteForce(A,m):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (A[i] + A[j]) % m == 0:
                count +=1
    return count
    
    
A=[1,7,6,13,8,17,11,18,19,9,21,23,26]
m = 7

def findPair(A,m):
    n = len(A)
    hm = {}
    count = 0
    # Find pairs of zero
    # nc2
    for i in range(n):
        if A[i] % m in hm:
            hm[A[i] % m ] +=1
        else:
            hm[A[i] % m ] = 1
    if 0 in hm:
        count += (hm[0] * (hm[0] - 1)) // 2
    a = 1
    b = m - a
    while a < b:
        if a in hm and b in hm:
            count += hm[a] * hm[b]
        a+=1
        b-=1
    return count
print(findPairBruteForce(A,m))
print(findPair(A,m))