def swap(A,p1,p2):
    A[p1],A[p2] = A[p2],A[p1]

def setIndex(A):
    n = len(A)
    p1 = 1
    p2 = n - 1
    ref = A[0]
    while p1 <= p2:
        if A[p1] <= ref:
            p1+=1
        elif A[p2] > ref:
            p2-=1
        else:
            swap(A,p1,p2)
            p1+=1
            p2-=1
    swap(A,0,p2)
    return p2

def pivot(A,s,e):
    ref = A[s]
    p1 = s+1
    p2 = e
    
    while p1 <= p2:
        if A[p1] <= ref:
            p1+=1
        elif A[p2] > ref:
            p2-=1
        else:
            swap(A,p1,p2)
            p1+=1
            p2-=1
    swap(A,p2,s)
    return p2

def quicksort(A,s,e):
    if s >= e:
        return
    p = pivot(A,s,e)
    quicksort(A,s,p-1)
    quicksort(A,p+1,e)
        
        
A=[10,3,8,15,6,12,2,18,7,15,14]
n = len(A)
s = 0
e = n - 1
quicksort(A,s,e)

def sortAlreadySorted(A):
    n = len(A)
    for i in range(n-2,-1,-1):
        if A[i] > A[i+1]:
            swap(A,i,i+1)
        else:
            break
    

def insertionSort(A):
    n = len(A)
    for i in range(n):
        for j in range(i-1,-1,-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
            else:
                break
A=[5,1,4,7,2,3,-1]   
insertionSort(A)

def generateParenthesis(n,o,c,s):
    if o == 0 and c == 0:
        print(s)
    if o > 0:
        generateParenthesis(n,o-1,c,s=s+'(')
    if c > o:
        generateParenthesis(n,o,c-1,s=s+')')
n = 2

generateParenthesis(n,n,n,'')