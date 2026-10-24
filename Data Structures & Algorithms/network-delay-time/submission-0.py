class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for [start, end, time] in times:
            adjList[start].append((end, time))
        
        queue = deque()
        visited = set()
        currTimes = defaultdict(int)

        queue.append(k)
        visited.add(k)
        currTimes[k] = 0
        while queue:
            curr = queue.popleft()
            for (x, time) in adjList[curr]:
                if x not in visited or currTimes[curr] + time < currTimes[x] :
                    visited.add(x)
                    currTimes[x] = currTimes[curr]+time
                    queue.append(x)
        return max(currTimes.values()) if len(visited) == n else -1
                
        

