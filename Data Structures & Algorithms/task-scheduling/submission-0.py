class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [] # (-freq, task)
        taskToFreq = defaultdict(int)
        for task in tasks:
            taskToFreq[task] += 1
        for task, freq in taskToFreq.items():
            heapq.heappush(heap, (-freq, task))
        
        ts = 1
        timedOut = deque() # (expire, newFreq, task)
        while heap or timedOut:
            while timedOut and timedOut[0][0] <= ts:
                _, freq, task = timedOut.popleft()
                heapq.heappush(heap, (freq, task))
            if heap:
                freq, task = heapq.heappop(heap)
                if freq+1 != 0:
                    timedOut.append((ts+n+1, freq+1, task))
                ts += 1
            else:
                ts = timedOut[0][0]
        return ts-1