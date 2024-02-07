weight = [2,6,5,3,4]
value = [6,20,15,12,10]
items = ["Mango","Apple","Banana","Kiwi",'Watermelon']
capacity = 8
n = len(weight)
def knapsackBruteForce(capacity,idx):
    if idx < 0:
        return 0
    if weight[idx] <= capacity:
        t = value[idx] + knapsackBruteForce(capacity - weight[idx],idx-1)
        dt = knapsackBruteForce(capacity,idx-1)
        return max(t,dt)
    else:
        return knapsackBruteForce(capacity,idx-1)

def generateDp(n,m):
    ans = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(-1)
        ans.append(temp)
    return ans
    

    
# dp = generateDp(n+1,capacity+1)

def knapsackOptimized(i,j):
    if i == 0 or j == 0:
        dp[i][j] = 0
        return dp[i][j]
    if dp[i][j] != -1:
        return dp[i][j]
    if weight[i-1] <= j:
        # Take
        t = value[i-1] + knapsackOptimized(i-1,j- weight[i-1])
        # Don't take
        dt = knapsackOptimized(i-1,j)
        dp[i][j] = max(t,dt)
        return dp[i][j]
    else:
        dp[i][j] = knapsackOptimized(i-1,j)
        return dp[i][j]


def getSelectedItems(dp,weight,value):
    i = len(dp) - 1
    j = len(dp[0]) - 1
    ans = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            # Did not pick the element
            i-=1
        else:
            ans.append((items[i-1],weight[i-1],value[i-1]))
            j-= weight[i-1]
            i-=1
    return ans
    

value = [2,3,5]
weight = [3,4,7]
capacity = 8
n = len(value)
dp = generateDp(n+1,capacity+1)
def unboundedKnapsack(i,j):
    if i == 0 or j == 0:
        dp[i][j] = 0;
        return dp[i][j]
    if dp[i][j] != -1:
        return dp[i][j]
    if weight[i-1] <= j:
        # Take
        t = value[i-1] +  unboundedKnapsack(i,j- weight[i-1])
        # Don't take
        dt = unboundedKnapsack(i-1,j)
        dp[i][j] = max(t,dt)
        return dp[i][j]
    else:
        dp[i][j] = unboundedKnapsack(i-1,j)
        return dp[i][j]
    
print(dp)
print(unboundedKnapsack(n,capacity))
 
        