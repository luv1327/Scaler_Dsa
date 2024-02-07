def isLowerCase(value):
    if ord(value) >= ord('a') and ord(value) <= ord('z'):
        return True
    return False

def toggleCase(A):
    n = len(A)
    print(A)
    for i in range(n):
        if isLowerCase(A[i]):
            A[i] = chr(ord(A[i]) - 32)
        else:
            A[i] = chr(ord(A[i]) + 32)
    print(A)
    
A=['a','b','c','A','E','d']

def sortInOrder(A):
    arr = [0] * 26
    n = len(A)
    for i in range(n):
        idx = ord(A[i]) - ord('a')
        arr[idx] +=1
    idx=0
    for i in range(len(arr)):
        char_to_fill = chr(i + ord('a'))
        time_to_fill = arr[i]
        for j in range(time_to_fill):
            A[idx] = char_to_fill
            idx+=1
    return A
        
    


def reverseStr(A,s,e):
    i = s
    j = e
    while i < j:
        A[i],A[j] = A[j],A[i]
        i+=1
        j-=1
    


A=['a','b','d','a','c','b','d','e','z'] 

def isPalindrome(A):
    n = len(A)
    i = 0
    j = n-1
    
    while i < j:
        if A[i] != A[j]:
            return False
        i+=1
        j-=1
    
    return True
A='abba'

def reverseStringWordByWord(A):
    n = len(A)
    s= 0
    e = 0
    for i in range(n):
        if A[i] == ' ':
            e=i- 1
            reverseStr(A,s,e)
            s= i+1
    e = n - 1
    reverseStr(A,s,e)
    return A
            
      
def checkPalindrome(A,l,r,n):
    while l >= 0 and r < n:
        if A[l] != A[r]:
            break
        l-=1
        r+=1
    return r - l - 1
        
              
    
def lengthOfLongestPalindromicSubString(A):
    n = len(A)
    ans = 0
    for i in range(n):
        l = i-1
        r = i+1
        ans = max(ans,checkPalindrome(A,l,r,n))
        ans = max(ans,checkPalindrome(A,l,r+1,n))
    
    return ans
        
    
A='abac'
