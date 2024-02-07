import math
def generateNumbers(A,idx,n):
    if idx == n:
        print(A)
        return
    A[idx] = 1
    generateNumbers(A,idx+1,n)
    A[idx] = 2
    generateNumbers(A,idx+1,n)
n = 2
idx = 0
A=[0] * n
# generateNumbers(A,idx,n)

def subsetsSumK(A,idx,k,s):
    if idx == len(A):
        if s == k:
            return 1
        return 0
    s+= A[idx]
    x = subsetsSumK(A,idx+1,k,s)
    s-= A[idx]
    y =subsetsSumK(A,idx+1,k,s)
    return x + y
    
A=[5,2,7]
idx = 0
k = 7
s = 0

def generateChessBoard(n):
    ans = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append('.')
        ans.append(temp)
    return ans

def canPlace(A,i,j,n):
    # Top
    row = i
    col = j
    while row >= 0:
        if A[row][col] == 'Q':
            return False
        row-=1
    

    # Left Diagonal
    row = i
    col = j
    while row >= 0 and col >= 0:
        if A[row][col] == 'Q':
            return False
        row-=1
        col-=1
    
    # Right Diagonal
    row = i
    col = j
    while row >= 0 and col < n:
        if A[row][col] == 'Q':
            return False
        row-=1
        col+=1
    
    return True
    

def nQueens(A,row,n):
    if row == n:
        for i in range(len(A)):
            print(A[i])
        return
    for col in range(n):
        if canPlace(A,row,col,n):
            A[row][col] = 'Q'
            nQueens(A,row+1,n)
            A[row][col] = '.'

# n=1
# A=generateChessBoard(n)
# row = 0
# nQueens(A,row,n)

def subsetsTwo(A,idx,arr):
    if idx == len(A):
        print(arr)
        return
    arr.append(A[idx])
    subsetsTwo(A,idx+1,arr)
    arr.pop()
    subsetsTwo(A,idx+1,arr)
    
A=[1,1]

hm = {
    "0" : '0',
    "1" : "1",
    "2": "abc", 
    "3": "def", 
    "4": "ghi", 
    "5": "jkl", 
    "6": "mno", 
    "7": "pqrs", 
    "8": "tuv", 
    "9": "wxyz"
}

A='012'

res = []

def generate(i,s):
    if len(s) == len(A):
        res.append(s)
        return
    for x in hm[A[i]]:
        generate(i+1,s = s+ x)
        
A=[1,2,2]  
A.sort()

res=[]
def generateSubsets(i,subset):
    if i == len(A):
        res.append(subset.copy())
        return
    subset.append(A[i])
    generateSubsets(i+1,subset)
    subset.pop()
    while i + 1 < len(A) and A[i] == A[i+1]:
        i+=1
    generateSubsets(i+1,subset)
        
    
    
A='a1b2'
res = []
n = len(A)

def isChar(s):
    if ord(s) >= ord('A') and ord(s) <= ord('z'):
        return True
    return False

res = []

def letterCasePermutations(i,s):
    if len(s) == n:
        res.append(s)
        return
    if isChar(A[i]) == True:
        if A[i].isupper() == True:
            letterCasePermutations(i+1,s=s+A[i].lower())
        else:
            letterCasePermutations(i+1,s=s+A[i].upper())
    letterCasePermutations(i+1,s=s+A[i])
        


        
i=0
s='' 
letterCasePermutations(i,s)

print(res)