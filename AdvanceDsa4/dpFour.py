def generateDp(n,m):
    ans = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(None)
        ans.append(temp)
    return ans

def reverseString(s):
    n = len(s)
    new_s = ''
    for i in range(n-1,-1,-1):
        new_s+=s[i]
    return new_s

A='klagrip'
B='lgigkm'
n = len(A)
m = len(B)
dp = generateDp(n,m)

def lcs(i,j):
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != None:
        return dp[i][j]
    if A[i] == B[j]:
        dp[i][j] = 1 + lcs(i-1,j-1)
    else:
        x = lcs(i-1,j)
        y = lcs(i,j-1)
        dp[i][j] = max(x,y)
    return dp[i][j]

i = len(A) - 1
j = len(B) - 1


A = "bebeeed"
n = len(A)
B=reverseString(A)
dp = generateDp(n,n)

def lcps(i,j):
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != None:
        return dp[i][j]
    
    if A[i] == B[j]:
        dp[i][j] = 1 + lcps(i-1,j-1)
    else:
        x = lcps(i-1,j)
        y = lcps(i,j-1)
        dp[i][j] = max(x,y)
    return dp[i][j] 

i = n - 1
j = n - 1

A = "Anshuman"
B = "Antihuman"
n = len(A)
m = len(B)
dp = generateDp(n,m)

def med(i,j):
    if i < 0 :
        return j+1
    if j < 0:
        return i+1
    if dp[i][j] != None:
        return dp[i][j]
    if A[i] == B[j]:
        dp[i][j] =  med(i-1,j-1)
    else:
        # Delete
        x = 1 + med(i-1,j)
        # Update
        y = 1 + med(i-1,j-1)
        # Insert
        z = 1 + med(i,j-1)
        dp[i][j] = min(x,y,z)
    return dp[i][j]

i = len(A) - 1
j = len(B) - 1

text = "acz"
pattern = "a?a"

dp = generateDp(i+1,j+1)

def wcm(i,j):
    if i < 0 and j < 0:
        return True
    if i < 0 and j >=0:
        return False
    if j < 0 and i >=0:
        for k in range(i+1):
            if pattern[k] != '*':
                return False
        return True
    if dp[i][j] != None:
        return dp[i][j]
    if pattern[i] == text[j] or pattern[i] == '?' :
        dp[i][j] = wcm(i-1,j-1)
        return dp[i][j]
    if pattern[i] == '*':
        dp[i][j] =  wcm(i-1,j) or wcm(i,j-1) 
        return dp[i][j]
    dp[i][j] = False
    return dp[i][j]
         



i = len(pattern)-1
j = len(text)-1
print(wcm(i,j))

    
    
