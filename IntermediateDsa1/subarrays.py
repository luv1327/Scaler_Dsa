def printSubArr(A,s,e):
    for i in range(s,e+1):
        print(A[i])
        
A=[10,4,5,19]

def printAllSubArr(A):
    n = len(A)
    for i in range(n):
        for j in range(i,n):
            total = 0
            for k in range(i,j+1):
                total += A[k]
            print(total)

def printAllSubArrWithPf(A):
    n = len(A)
    pf = [0] * n
    pf[0] = A[0]
    for i in range(1,n):
        pf[i] = pf[i-1] + A[i]
    for i in range(n):
        for j in range(i,n):
            if i > 0:
                print(pf[j]-pf[i-1])
            else:
                print(pf[j])
                
    
            
def printAllSubArraySumCarryForward(A):
    n = len(A)
    ans = 0
    for i in range(n):
        total = 0
        for j in range(i,n):
            total += A[j]
            ans += total
    return ans
A=[6,8,-1,7] 

def allSubArraySumWithContributionTecnique(A):
    n = len(A)
    total = 0
    for i in range(n):
        # contribution = (i-0+1) * (n-1 - i + 1)
        # on the basis of s and e e-s+1
        contribution = (i+1) * (n-i)
        total += A[i] * contribution
    return total

print("Total",allSubArraySumWithContributionTecnique(A))