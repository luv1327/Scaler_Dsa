def pow(a,n):
    if n == 1:
        return a
    return a * pow(a,n-1)

def powOptimised(a,n):
    if n == 1:
        return a
    ha = pow(a,n//2)
    if n % 2 == 0:
        return ha * ha
    else:
        return ha * ha * a
    
def powModulo(a,n,m):
    if n == 1:
        return a
    ha = powModulo(a,n//2,m)
    if n % 2 == 0:
        return (ha * ha) % m 
    else:
        return (ha * ha * a )% m
    
print(powModulo(2,4,2))