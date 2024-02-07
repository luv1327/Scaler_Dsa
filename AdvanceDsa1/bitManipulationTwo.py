def checkBit(n,i):
    if (n >> i) & 1 == 1:
        return True
    return False

def findSetBit(n):
    for i in range(32):
        if (n >> i) & 1 == 1:
            return i

def findTwoElements(A):
    n = len(A)
    s = set()
    ans = []
    for i in range(n):
        s.add(A[i])
    for i in range(1,n+3):
        if i not in s:
            ans.append(i)
    return ans

def findTwoNonRepeatingElement(A):
    n = len(A)
    res = 0 
    ans = []
    for i in range(n):
        res = res ^ A[i] 
    for i in range(1,n+3):
        res = res ^ i   
    ith_set_bit = findSetBit(res)
    temp = res
    for i in range(n):
        if  checkBit(A[i],ith_set_bit):
            temp = temp ^ A[i]
    ans.append(temp)
    ans.append(temp ^ res)
    return ans
    
A=[3,6,1,2]

def findMaxIJBruteForce(A):
    n = len(A)
    ans = float('-inf')
    for i in range(n):
        for j in range(i+1,n):
            ans = max(ans,A[i] & A[j])
    return ans



def findMaxIJ(A):
    n = len(A)
    ans = 0
    for i in range(31,-1,-1):
        count = 0
        for j in range(n):
            if checkBit(A[j],i):
                count +=1
        if count >=2:
            ans += 2 ** i
            for j in range(n):
                if checkBit(A[j],i) == False:
                    A[j] = 0
    return ans
A=[26,13,23,28,27,7,25]
print(findMaxIJBruteForce(A))
print(findMaxIJ(A))
