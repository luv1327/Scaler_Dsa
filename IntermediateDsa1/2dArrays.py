
def rowWiseSum(A):
    n = len(A)
    for i in range(n):
        current_sum = 0
        for j in range(n):
            current_sum += A[i][j]
        print(current_sum)
        
def columnWiseSum(A):
    n = len(A)
    m = len(A[0])
    for j in range(m):
        current_sum = 0
        for i in range(n):
            current_sum += A[i][j]
        print(current_sum)
        
def printDiagonal(A):
    n = len(A)
    m = len(A[0])
    i = 0
    j = 0
    while i < n and j < m:
        # print(A[i][j])
        i+=1
        j+=1
    i = 0
    j = m-1
    while i < n and j >= 0:
        print(A[i][j])
        i+=1
        j-=1
        
        
def printAllDiagonals(A):
    n = len(A)
    for c in range(n):
        i = 0
        j =  c
        while i < n and j>=0:
            print(A[i][j])
            i+=1
            j-=1
    
    for c in range(1,n):
        i = c
        j = n - 1
        while i < n and j >= 0:
            print(A[i][j])
            i+=1
            j-=1
            
def reverseArr(A):
    n =len(A)
    s = 0
    e = n - 1
    while s < e:
        A[s],A[e] = A[e],A[s]
        s+=1
        e-=1

def swap(A,i,j):
    A[i][j],A[j][i] = A[j][i],A[i][j]
     
def transpose(A):
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            swap(A,i,j) 
    for i in range(n):
        reverseArr(A[i]) 
        print(A[i])
    
A=[
    [1,  2, 3, 4, 5],
    [6,  7, 8, 9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]


transpose(A)
