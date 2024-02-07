import heapq
from collections import deque

def generateAdjList(A):
    hm = {}
    n = len(A)
    for i in range(n):
        source = A[i][0]
        destination = A[i][1]
        time = A[i][2]
        val1 = (time,destination)
        val2 = (time,source)
        if source in hm:
            hm[source].append(val1)
        else:
            hm[source] = [val1]
        
        if destination in hm:
            hm[destination].append(val2)
        else:
            hm[destination] = [val2]
    return hm


def minPath(A,nodes,source):
    adj = generateAdjList(A)
    distance = [float('+inf')] * (nodes+1)
    distance[source] = 0
    pq = []
    heapq.heappush(pq,(distance[source],source))
    while len(pq) > 0:
        busted = pq[0]
        heapq.heappop(pq)
        parent_time = busted[0]
        src = busted[1]
        if src in adj:
            for x in adj[src]:
                next_pump = x[1]
                next_pump_time = x[0]
                total_time = next_pump_time + parent_time
                if total_time < distance[next_pump]:
                    val = (total_time,next_pump)
                    distance[next_pump] = total_time
                    heapq.heappush(pq,val)
    return distance
        
    

nodes = 6
A = [   [0, 4, 9],
        [3, 4, 6] ,
        [1, 2, 1] ,
        [2, 5, 1] ,
        [2, 4, 5] ,
        [0, 3, 7] ,
        [0, 1, 1] ,
        [4, 5, 7] ,
        [0, 5, 1] ,] 
source = 4   

def createAdjList(A,tasks):
    n = len(A)
    hm = {}
    for i in range(n):
        source = A[i][0]
        destination = A[i][1]
        tasks[destination] +=1
        if source in hm:
            hm[source].append(destination)
        else:
            hm[source] = [destination]
    return hm  


#  Use min heap for lexogeographically sorted list
                
def topologicalSort(A,n):
    tasks = [0] * (n+1)
    adj = createAdjList(A,tasks)
    q = deque()
    ans = []
    for i in range(len(tasks)):
        # i != 0 for 0 index
        if tasks[i] == 0 and i != 0:
            ans.append(i)
            q.append(i)
    while len(q) > 0:
        completed_task = q[0]
        q.popleft()
        if completed_task in adj:
            for x in adj[completed_task]:
                tasks[x] -=1
                if tasks[x] == 0:
                    ans.append(x)
                    q.append(x)
    return ans
    


A = [  
     [1,2],
     [2,3],
     [3,4],
     [4,1],
     [5,1],
]
n= 5
  
topologicalSort(A,n)      
        
        
        
        
    
