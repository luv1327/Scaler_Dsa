def isOdd(num):
    if num & 1:
        return True
    return False

def checkBit(num,i):
    if (num >> i) & 1 == 1:
        return True
    return False

def checkNumberOfSetBit(num):
    count = 0
    while num > 0:
        if isOdd(num):
            count +=1 
        num = num >> 1
    return count


def setBit(num,i):
    a = 1 << i
    return num | a
    
print(setBit(10,2))

