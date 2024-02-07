def nNaturalNumber(n):
    if n == 1:
        return n
    return nNaturalNumber(n-1) + n

def fact(n):
    if n == 1:
        return n
    return fact(n-1) * n

def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

def printInIncrease(n):
    if n == 1:
        print(n)
        return
    printInIncrease(n-1)
    print(n)
    
def isPalindrome(A,s,e):
    if s >= e:
        return True
    if A[s] == A[e]:
        return isPalindrome(A,s=s+1,e=e-1)
    return False
    
A='goodog'
n = len(A)
s=0
e=n-1
print(isPalindrome(A,s,e))