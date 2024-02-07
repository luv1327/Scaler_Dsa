def findSetBit(n):
    for i in range(32):
        if (n >> i) & 1 == 1:
            return i

def checkBit(n,i):
    if (n >> i) & 1 == 1:
        return True
    return False
        

def findTwoNonRepeatingElement(A):
    n = len(A)
    res = 0 
    ans = []
    for i in range(n):
        res = res ^ A[i]
    
    ith_set_bit = findSetBit(res)
    temp = res
    for i in range(n):
        if  checkBit(A[i],ith_set_bit):
            temp = temp ^ A[i]
    ans.append(temp)
    ans.append(temp ^ res)
    return ans
       
A=[1,3,4,5,7,1,3,5,4,9]

def findUniqueElement(A):
    n = len(A)
    arr = [0] * 32
    ans = 0
    for i in range(n):
        for j in range(32):
            if checkBit(A[i],j):
                arr[j] +=1
    for i in range(len(arr)):
        arr[i] = arr[i] % 3
    for i in range(len(arr)):
        ans += 2 ** i * arr[i]
    return ans
        
    
A=[2,2,2,3,3,3,4,4,4,1000,9,9,9]

print(findUniqueElement(A))
