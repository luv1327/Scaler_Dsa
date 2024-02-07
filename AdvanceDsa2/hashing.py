def countFreq(A):
    n = len(A)
    arr = [0] * 6
    for i in range(n):
        arr[A[i]] +=1
    for i in range(len(arr)):
        print(i,arr[i])
    
A=[2,3,5,5,3,0,2,0,1]

def findMinAbsBruteForce(A):
    n = len(A)
    min_val = float('+inf')
    for i in range(n):
        for j in range(i+1,n):
            if A[i] == A[j]:
                current_val = abs(j-i)
                min_val = min(min_val,current_val)
    return min_val
                
   
def findMinAbsDistance(A):
    n = len(A)
    hm = {}
    min_val = float('+inf')
    for i in range(n):
        if A[i] in hm:
            current_val = abs(hm[A[i]] - i)
            min_val =   min(min_val,current_val)
            hm[A[i]] = i
        else:
            hm[A[i]] = i
    return min_val      
A=[2,3,5,7,2,6,5,7,3,5,7]

def findLongestSequence(A):
    n = len(A)
    s = set()
    max_count = float('-inf')
    for i in range(n):
        s.add(A[i])
    for i in range(n):
        val = A[i]
        lesser = val - 1
        if lesser in s:
            pass
        else:
            current_count = 1
            current_val = val + 1
            while current_val in s:
                current_count +=1
                current_val +=1
            max_count = max(max_count, current_count)
    return max_count
            
            
    
A=[100,4,3,6,10,20,11,7,5,101,102]

print(findLongestSequence(A))

