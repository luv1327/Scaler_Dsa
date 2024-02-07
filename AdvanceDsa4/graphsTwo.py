from collections import deque

N=[6,6,6,8,8,9,5,4,3,3,3,2,2,16,1]
M=[7,8,5,9,10,11,4,3,13,12,2,1,16,15,14]

def generateAdjList(N,M,isUndirected=True):
    n = len(N)
    hm = {}
    for i in range(n):
        source = N[i]
        destination = M[i]
        if source in hm:
            hm[source].append(destination)
        else:
            hm[source] = [destination]
        
        if isUndirected and destination in hm:
            hm[destination].append(source)
        else:
            hm[destination] = [source]
    return hm
        
path = []
def dfs(source,adj,visited,destination):
    if visited[source]:
        return
    visited[source] = True
    if destination == source:
        path.append(source)
        print(path)
        return
    path.append(source)
    if source in adj:
        for x in adj[source]:
            dfs(x,adj,visited,destination)
    path.pop()
    

def helper(N,M,source,destination):
    adj = generateAdjList(N,M)
    n=max(max(N),max(M))
    visited = [False] * (n+1)
    dfs(source,adj,visited,destination)
    return visited[destination]
    
    
    
N=[1,1,2,2,3,6,6,7,8,10,12,12]
M=[2,3,4,5,5,7,8,9,9,11,13,14]

def dfs(source,adj,visited):
    if visited[source]:
        return 
    visited[source] = True
    if source in adj:
        for x in adj[source]:
            dfs(x,adj,visited)

def findNumberOfComponents(N,M):
    n = max(max(N),max(M))
    visited = [False] * (n+1)
    adj = generateAdjList(N,M)
    component_count = 0
    for i in range(len(N)):
        source = N[i]
        if visited[source] == False:
            dfs(source,adj,visited)
            component_count +=1
    return component_count
        
        
def isCyclic(A,N,M):
    component_count = findNumberOfComponents(N,M)
    max_edges = A - component_count
    if len(M) > max_edges:
        return True
    return False
    
A=[
    [1,1,0,0,1],
    [0,1,0,1,0],
    [1,0,0,1,1],
    [1,1,0,0,0],
    [1,0,1,1,1]
]

def dfs(i,j,A):
    if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]):
        return
    if A[i][j] != 1:
        return
    A[i][j] = -1
    dfs(i-1,j,A)
    dfs(i+1,j,A)
    dfs(i,j+1,A)
    dfs(i,j-1,A)


def helper(A):
    n = len(A)
    m = len(A[0])
    island_count = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                dfs(i,j,A)
                island_count +=1
    return island_count

def canRot(i,j,n,m,A):
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    if A[i][j] == 1:
        return True
    return False

def rottenOranges(A):
    n = len(A)
    m = len(A[0])
    q = deque()
    for i in range(n):
        for j in range(m):
            if A[i][j] == 2:
                q.append((i,j))
    last = q[len(q) - 1]
    time = 0
    while len(q) > 0:
        front = q[-1]
        q.popleft()
        i = front[0]
        j = front[1]
        A[i][j] = 2
        if canRot(i+1,j,n,m,A):
            q.append((i+1,j))
        if canRot(i-1,j,n,m,A):
            q.append((i-1,j))
        if canRot(i,j+1,n,m,A):
            q.append((i,j+1))
        if canRot(i,j-1,n,m,A):
            q.append((i,j-1))
        if front == last:
            time +=1
            if len(q) > 0:
                last = q[-1]
    return time
        
    
A = [   [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
]
    
print(A)
print(rottenOranges(A))
    