import heapq

def getItemsProtienPerKg(A,B):
    n = len(A)
    protien_per_kg = []
    for i in range(n):
        item_in_kg = A[i]
        protien = B[i]
        per_kg = protien / item_in_kg
        protien_per_kg.append((per_kg,item_in_kg))
    return protien_per_kg
        
    

def maxProtien(A,B,C):
    protien_per_kg = getItemsProtienPerKg(A,B)
    protien_per_kg.sort(reverse=True)
    n = len(protien_per_kg)
    kg = C
    total_intake = 0
    for i in range(n):
        protien_per_kg_in_item = protien_per_kg[i][0]
        item_in_kg = protien_per_kg[i][1]
        protien_value = item_in_kg * protien_per_kg_in_item
        if kg >= item_in_kg:
            total_intake += protien_value
            kg-= item_in_kg
        else:
            total_intake += kg * protien_per_kg_in_item
            break
    return int(total_intake * 100)
        
    


A=[20,15,50,10,25,12,5]
B=[200,180,250,150,200,132,100]
C = 70

def takeSecond(A):
    return A[1]

def sortByActivity(A,B):
    n = len(A)
    activities = []
    for i in range(n):
        start_time = A[i]
        end_time = B[i]
        activities.append((start_time,end_time))
    activities.sort(key=takeSecond)
    return activities



def activitySelection(A,B):
    activities = sortByActivity(A,B)
    n = len(activities)
    count = 1
    current_activity_start_time = activities[0][0]
    current_activity_end_time = activities[0][1]
    for i in range(1,n):
        start_time = activities[i][0]
        end_time = activities[i][1]
        if start_time >= current_activity_end_time:
            current_activity_start_time = start_time
            current_activity_end_time = end_time
            count +=1
    return count
    
    
    
A = [5, 1, 3, 0, 5, 8]
B = [9, 2, 4, 6, 7, 9]
activitySelection(A,B)

def sortByDeadline(A,B):
    n =len(A)
    jobs = []
    for i in range(n):
        deadline = A[i]
        profit = B[i]
        jobs.append((deadline,profit))
    jobs.sort()
    return jobs

def jobSchedule(A,B):
    jobs = sortByDeadline(A,B)
    min_heap = []
    n = len(jobs)
    for i in range(n):
        deadline = jobs[i][0]
        profit = jobs[i][1]
        if deadline > len(min_heap):
            heapq.heappush(min_heap,profit)
        else:
            if len(min_heap) > 0:
                if profit > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,profit)
    return sum(min_heap)
    
    

A=[1,1,1,2,2,4,4,5,5]
B=[200,50,350,200,150,250,140,600,400]

def getMinimumCost(A,B,C):
    min_heap = []
    for i in range(B):
        heapq.heappush(min_heap,C[i])
    passengers = A
    ans = 0
    while passengers > 0:
        front = min_heap[0]
        heapq.heappop(min_heap)
        ans+=front
        passengers -=1
        front -= 1
        if front > 0:
            heapq.heappush(min_heap,front)
    return ans

def getMaximumCost(A,B,C):
    max_heap = []
    for i in range(B):
        heapq.heappush(max_heap,-C[i])
    passengers = A
    ans = 0
    while passengers > 0:
        front = -max_heap[0]
        heapq.heappop(max_heap)
        ans += front
        passengers -=1
        front -=1
        if front > 0 :
            heapq.heappush(max_heap,-front)
    return ans


def shipMaxMin(A,B,C):
    max_cost = getMaximumCost(A,B,C)
    min_cost = getMinimumCost(A,B,C)
    return [max_cost,min_cost]
    
A = 4
B = 3
C = [2, 1, 1]

def coinProblem(A):
    max_heap = []
    for i in range(A):
        val = 5 ** i
        if val <= A:
            heapq.heappush(max_heap,-val)
        else:
            break
    count = 0
    while A > 0 and len(max_heap) > 0:
        front = -max_heap[0]
        if front > A:
            heapq.heappop(max_heap)
        else:
            count +=1
            A-= front
            if front > A:
                heapq.heappop(max_heap)
    return count

def coin(A):
    ans = 0
    while (A > 0):
        ans += (A % 5)
        A = A // 5
    return int(ans)

    
            
    
def seats(A):
    n = len(A)
    min_ans = float('+inf')
    for i in range(n):
        if A[i] == 'x':
            ans = 0
            adjacent_count_left = 0
            adjacent_count_right = 0
            for x in range(i+1,n):
                if A[x] != 'x':
                    break
                else:
                    adjacent_count_right +=1
            for x in range(i-1,-1,-1):
                if A[x] != 'x':
                    break
                else:
                    adjacent_count_left +=1
            for j in range(i+1,n):
                if A[j] == 'x':
                    ans+= j-i-1
            for j in range(i-1,-1,-1):
                    if A[j] == 'x':
                        ans+=i-j-1
            # ans -= (adjacent_count_left+adjacent_count_right)
            print(ans)
            min_ans = min(ans,min_ans)
    print(min_ans)
    

def seatsSliding(A):
    n = len(A)
    k=0
    indexes = []
    for i in range(n):
        if A[i] == 'x':
            indexes.append(i)
            k+=1
    l = 0
    r = k
    ans=float('+inf')
    while r <= n:
        window_indexes = []
        for i in range(l,r):
            window_indexes.append(i)
        diff = 0
        for x in range(len(indexes)):
            diff += abs(indexes[x] - window_indexes[x])
        ans=min(ans,diff)    
        l+=1
        r+=1
    return ans

def seatsSlidingOptimised(A):
    n = len(A)
    indexes = []
    for i in range(n):
        if A[i] == 'x':
            indexes.append(i)
    mid = len(indexes) // 2
    left = indexes[mid] - 1
    right = indexes[mid] + 1
    k = 1
    ans = 0
    while left >= 0:
        ans += (indexes[mid]-k)-left
        left-=1
        k+=1
    k = 1
    
    while right < n:
        ans += (indexes[mid] - k )- right
        right +=1
        k+=1
    print(ans)
        
        
A = "....x..xx...x.."

def subSets(A,idx,arr,matrix):
    if idx == len(A):
        matrix.append(arr.copy())
        return
    
    arr.append(A[idx])
    subSets(A,idx+1,arr,matrix)
    arr.pop()
    subSets(A,idx+1,arr,matrix)
    
    
        
    
A = [1,1]
matrix = []
idx = 0
subSets(A,idx,[],matrix)

print(matrix)


