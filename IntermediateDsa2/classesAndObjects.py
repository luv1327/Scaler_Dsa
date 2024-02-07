class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    
    def area(self):
        return self.l * self.b
    
    def isSquare(self):
        if self.l == self.b:
            return True
        return False
    
Length = [2,5,3,6,2]
Breadth = [4,5,1,6,2]

def totalSum(A,B):
    n = len(A)
    ans = 0
    for i in range(n):
        l = A[i]
        b = B[i]
        new_rectangle = Rectangle(l,b)
        if new_rectangle.isSquare() == False:
            ans += new_rectangle.area()
            
    return ans

print(totalSum(Length,Breadth))