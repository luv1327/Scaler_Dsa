def specialIndex(A):
    n = len(A)
    pf_even = [0] * n
    pf_odd = [0] * n
    pf_even[0] = A[0]
    pf_odd[0] = 0
    count = 0
    for i in range(1,n):
        if i % 2 == 0:
            pf_even[i] = pf_even[i-1] + A[i]
        else:
            pf_even[i] = pf_even[i-1] 
        
        if i % 2 != 0:
            pf_odd[i] = pf_odd[i-1] + A[i]
        else:
            pf_odd[i] = pf_odd[i-1]
    
    for i in range(n):
        if i > 0:
            even_sum = pf_even[i-1] + pf_odd[n-1] - pf_odd[i]
            odd_sum = pf_odd[i-1] + pf_even[n-1] - pf_even[i]
            if odd_sum == even_sum:
                count +=1
        else:
            even_sum = pf_even[n-1] - pf_even[i]
            odd_sum = pf_odd[n-1] - pf_odd[i]
            if even_sum == odd_sum:
                count +=1
    return count
                
    
A=[4,3,2,7,6,-2]

def mooresVoting(A):
    n = len(A)
    count = 1
    majority_element = A[0]
    for i in range(1,n):
        if majority_element == A[i]:
            count +=1
        else:
            count -=1
        
        if count == 0:
            majority_element = A[i]
            count +=1
    count = 0
    for i in range(n):
        if A[i] == majority_element:
            count +=1
    
    if count > n//2:
        return majority_element
    return -1
    
A=[1,2,8,1,5,1,1,3]
print(mooresVoting(A))