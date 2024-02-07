def isTriangle(p1,p2,p3):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    if (x1 == x2 and y1 == y3) or (x1 == x3 and y1 == y2):
        return True
    if (x2 == x3 and y2 == y1) or (x2 == x1 and y2 == y3):
        return True
    if (x3 == x1 and y3 == y2) or (x3 == x2 and y3 == y1):
        return True
    return False 


def countTriangle(A,B):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                p1 = (A[i],B[i])
                p2 = (A[j],B[j])
                p3 = (A[k],B[k])
                if isTriangle(p1,p2,p3):
                    count +=1
    return count
    
A=[1,1,3,5,5]
B=[1,3,3,1,3]


def countTrainglesOptimised(A,B):
    n = len(A)
    hmx = {}
    hmy = {}
    count = 0
    for i in range(n):
        if A[i] in hmx:
            hmx[A[i]] += 1
        else:
            hmx[A[i]] = 1
        if B[i] in hmy:
            hmy[B[i]] +=1
        else:
            hmy[B[i]] = 1
    for i in range(n):
        count_x = hmx[A[i]]
        count_y = hmy[B[i]]
        count += (count_x-1) * (count_y -1)
    
    return count 
    
    
def countNumberOfRectangles(A,B):
    n = len(A)
    s = set()
    count = 0
    for i in range(n):
        val = (A[i],B[i])
        s.add(val)
    for i in range(n):
        for j in range(i+1,n):
            x1 = A[i]
            y1 = B[i]
            x2 = A[j]
            y2 = B[j]
            a = (x1,y2)
            b = (x2,y1)
            if x1 == x2 or y1 == y2:
                continue 
            if a in s and b in s:
                count +=1
    return count // 2 

A = [1, 1, 2, 2, 3, 3]
B = [1, 2, 1, 2, 1, 2]

def checkPermutation(hma,hmb):
    flag = True
    for x in hma:
        if x not in hmb:
            flag = False
        if x in hmb:
            if hmb[x] != hma[x]:
                flag = False
    return flag

def countPermutations(A,B):
    hma = {}
    hmb = {}
    k = len(A)
    count = 0
    for i in range(k):
        if A[i] in hma:
            hma[A[i]] +=1
        else:
            hma[A[i]] = 1
        if B[i] in hmb:
            hmb[B[i]] +=1
        else:
            hmb[B[i]] = 1
    if checkPermutation(hma,hmb):
        count +=1
    l = 1
    r = k
    n = len(B)
    while r < n:
        hmb[B[l-1]] -=1
        if hmb[B[l-1]] <= 0:
            del hmb[B[l-1]]
        if B[r] in hmb:
            hmb[B[r]] +=1
        else:
            hmb[B[r]] = 1
        if checkPermutation(hma,hmb):
            count +=1
        l+=1
        r+=1
    return count
        
    
    
A='abac'
B='abcaacbb'

print(countPermutations(A,B))