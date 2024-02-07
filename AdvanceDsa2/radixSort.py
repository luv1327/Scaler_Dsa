def printNNumbers(A,n):
    arr = [0] * (n+1)
    for i in range(len(A)):
        arr[A[i]] +=1
    for i in range(len(arr)):
        for j in range(arr[i]):
            print(i)
    
    
def sortTheArr(A,n):
    arr = [0] * (n+1)
    for i in range(len(A)):
        arr[A[i]] +=1
    idx = 0
    for i in range(len(arr)):
        for j in range(arr[i]):
            A[idx] = i
            idx+=1
    return A
        
        
    
n = 20
A=[2,5,1,0,19,15,12,1,13,2,5]


def sortArr(A):
    arr = [0] * 21
    for i in range(len(A)):
        idx = A[i] + 10
        arr[idx] +=1
    idx = 0
    for i in range(len(arr)):
        for j in range(arr[i]):
            A[idx] = i - 10
            idx +=1
    print(A)
    
A=[-5,7,1,0,-3,1,2,-5,-2,-3,-1]



def getNum(n,k):
    return (n // (10 ** k)) % 10

def generateMatrix():
    ans = []
    for i in range(10):
        ans.append([])
    return ans

def radix(A,k):
    n = len(A)
    arr = generateMatrix()
    for i in range(n):
        idx = getNum(A[i],k)
        arr[idx].append(A[i])
    print(arr)
    
A=[5,1001,211,322,433,567,376]

def sortByRadix(A):
    max_num = max(A)
    k = len(str(max_num))
    radix(A,0)
    
sortByRadix(A)
