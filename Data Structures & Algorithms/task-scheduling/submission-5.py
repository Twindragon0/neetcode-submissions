class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = defaultdict(int)
        for task in tasks:
            taskFreq[task] += 1
        available = [(-freq, task) for (task, freq) in taskFreq.items()]
        heapq.heapify(available)
        heap = []
        curr = 0
        while available or heap:
            while heap and heap[0][0] <= curr:
                _, freq, task = heapq.heappop(heap)
                heapq.heappush(available, (freq, task))
            if available:
                freq, task = heapq.heappop(available)
                if freq+1 != 0:
                    heapq.heappush(heap, (curr+n+1, freq+1, task))
                curr += 1
            else:
                x, freq, task = heapq.heappop(heap)
                curr = x
                if freq+1 != 0:
                    heapq.heappush(heap, (curr+n+1, freq+1, task))
                curr += 1
        return curr




