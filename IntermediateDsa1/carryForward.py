def countAGBruteForce(A):
    n = len(A)
    pairs = 0
    for i in range(n):
        for j in range(i+1,n):
            if A[i] == 'a' and A[j] == 'g':
                pairs +=1
    return pairs
    
A=['b','a','a','g','d','c','a','g']

def countAGOptimised(A):
    n = len(A)
    count_g = 0
    pairs = 0
    for i in range(n-1,-1,-1):
        if A[i] == 'g':
            count_g +=1
        if A[i] == 'a':
            pairs += count_g
    return pairs
            

def countLeaders(A):
    n = len(A)
    leaders_count = 1
    max_on_right = A[n-1]
    for i in range(n-2,-1,-1):
        if A[i] > max_on_right:
            leaders_count +=1
            max_on_right = A[i]
    return leaders_count
    
A=[5,7,6,1,-1,0,5,2]

def replaceLeaders(A):
    n = len(A)
    A.append(-1)
    max_on_right = A[n-1]
    for i in range(n-2,-1,-1):
        if A[i] > max_on_right:
            max_on_right = A[i]
        else:
            A[i] = max_on_right
    A.pop(0)
    return A
        
        
def findMinMaxClosest(A):
    n = len(A)
    min_length = float('+inf')
    max_element = max(A)
    min_element = min(A)
    if min_element == max_element:
        return 1
    for i in range(n):
        if A[i] == min_element:
            for j in range(i+1,n):
                if A[j] == max_element:
                    current_length = j-i+1
                    min_length = min(min_length,current_length)
                    break
        if A[i] == max_element:
            for j in range(i+1,n):
                if A[j] == min_element:
                    current_length = j-i+1
                    min_length = min(min_length,current_length)
                    break
    return min_length

A=[2,2,6,4,5,1,5,2,6,4,1]
print(findMinMaxClosest(A))

