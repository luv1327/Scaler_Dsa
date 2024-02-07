def swap(A,i,j):
    A[i],A[j] = A[j],A[i]

def findKthSmallest(A,k):
    n = len(A)
    for i in range(k):
        min_element = float('+inf')
        idx = -1
        for j in range(i,n):
            if A[j] < min_element:
                min_element = A[j]
                idx = j
                
        swap(A,i,idx)
    return A[k-1]
            
A=[2,8,4,-1,6,7,5,10,-1]
k=2


def selectionSort(A):
    n = len(A)
    for i in range(n):
        min_element = float('+inf')
        idx = -1
        for j in range(i,n):
            if A[j] < min_element:
                min_element = A[j]
                idx = j
        if idx != -1:
            swap(A,i,idx)
    return A

def mergeAB(A,B):
    n = len(A)
    m = len(B)
    C=[]
    p1 = 0
    p2 = 0
    
    while p1 < n and p2 < m:
        if A[p1] < B[p2]:
            C.append(A[p1])
            p1+=1
        else:
            C.append(B[p2])
            p2+=1
    
    while p1 < n:
        C.append(A[p1])
        p1+=1
    
    while p2 < m:
        C.append(B[p2])
        p2+=1
    
    return C

A=[7,9,10,11,14,17,18]
B=[3,8,9,12]

inversion_count = 0

def merge(A,s,m,e):
    global inversion_count
    C = []
    p1 = s
    p2 = m+1
    while p1 <= m and p2 <= e:
        if A[p1] < A[p2]:
            C.append(A[p1])
            p1+=1
        else:
            inversion_count += m - p1 + 1
            C.append(A[p2])
            p2+=1
    
    while p1 <= m:
        C.append(A[p1])
        p1+=1
    
    while p2 <= e:
        C.append(A[p2])
        p2+=1
    
    for i in range(len(C)):
        A[s+i] = C[i]


# A=[4,8,-1,2,6,9,11,3,4,7,13,-7]


def mergeSort(A,s,e):
    if s >= e:
        return 
    mid = (s+e) // 2
    mergeSort(A,s,mid)
    mergeSort(A,mid+1,e)
    merge(A,s,mid,e)
A = [1, 3, 2]
s=0
e=len(A) - 1
mergeSort(A,s,e)

print(inversion_count)