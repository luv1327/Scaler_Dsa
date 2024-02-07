from collections import deque

N=[1,1,2,2,3,5]
M=[2,4,4,3,5,6]

def generateAdjMatrix(N,M,isUndirected):
    n = len(N)
    hm = {}
    for i in range(n):
        source = N[i]
        destination = M[i]
        if source in hm:
            hm[source].append(destination)
        else:
            hm[source] = [destination]
        if isUndirected:
            if destination in hm:
                hm[destination].append(source)
            else:
                hm[destination] = [source]
    return hm
        
def bfs(N,M,s,d):
    n = len(N)
    adj = generateAdjMatrix(N,M,True)
    visited = [False] * (n+1)
    q = deque()
    q.append(s)
    visited[s] = True
    while len(q) > 0:
        source = q[0]
        q.popleft()
        if source in adj:
            for x in adj[source]:
                if visited[x] == False:
                    visited[x] = True
                    q.append(x)
    return visited[n]



def minDistance(N,M,s,d):
    n = len(N)
    adj = generateAdjMatrix(N,M,True)
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    q = deque()
    q.append(s)
    visited[s] = True
    while len(q) > 0:
        source = q[0]
        q.popleft()
        if source in adj:
            for x in adj[source]:
                if x == d:
                    return distance[source] + 1
                if visited[x] == False:
                    visited[x] = True
                    distance[x] = 1 + distance[source]
                    q.append(x)
    return distance[d]
                    
    
    

    