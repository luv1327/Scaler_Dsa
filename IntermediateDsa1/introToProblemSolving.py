import math
def countFactors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count +=1
    return count

def countFactorsOptimised(n):
    count = 0
    r = int(math.sqrt(n))
    for i in range(1,r+1):
        if n % i == 0:
            if i * i == n:
                count +=1
            else:
                count +=2
    return count
        
def isPrime(n):
    count = countFactorsOptimised(n)
    if count == 2:
        return True
    return False
    
def total(n):
    ans = n * (n+1) // 2
    return ans

def isPerfectSquare(n):
    for i in range(1,n):
        if i * i == n:
            return i
    return None

print(total(3))
            
    
