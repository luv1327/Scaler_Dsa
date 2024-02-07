from functools import cmp_to_key
import random

def findMin(A):
    n = len(A)
    A.sort(reverse=True)
    total_sum = sum(A)
    min_sum = 0
    for i in range(n):
        min_sum += total_sum
        total_sum-=A[i]
    return min_sum
    
    
A=[2,1,4]

def nobleInteger(A):
    n = len(A)
    noble_count = 0
    for i in range(n):
        local_count = 0
        for j in range(n):
            if A[i] > A[j]:
                local_count +=1
        if local_count == A[i]:
            noble_count +=1
    return noble_count


def nobleIntegerOptimised(A):
    n = len(A)
    A.sort()
    noble_count = 0
    for i in range(n):
        if A[i] == i:
            noble_count +=1
    return noble_count
   

def nobleIntegerDistinct(A):
    n = len(A)
    A.sort()
    noble_count = 0
    if A[0] == 0:
        noble_count +=1
    for i in range(1,n):
        if A[i] != A[i-1]:
            if A[i] == i:
                noble_count+=1
    return noble_count
                 
def compare(a,b):
    fa = a
    fb = b
    if fa < fb :
        return -1
    elif fa > fb :
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0 
    
def sortByComparison(A):
    sorted(A,key=cmp_to_key(compare))


def generateRandom():
    A=[]
    for i in range(10):
        A.append(random.randint(10,100))
    return A

A=generateRandom()
print(A)

print(sortByComparison(A))

