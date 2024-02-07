def sumOfN(n):
    if n == 1:
        return n
    return sumOfN(n-1) + n

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def printInDec(n):
    if n == 1:
        print(n)
        return 
    print(n)
    printInDec(n-1)
    
def toh(N,A,C,B):
    if N == 0:
        return
    toh(N-1,A,B,C)
    print(N,A,C)
    toh(N-1,B,C,A)
    
    
toh(3,"A","C","B")
