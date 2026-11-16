class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        heap = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        heapq.heapify(heap)
        ans = []
        curr = 1
        while available or heap:
            while heap and heap[0][0] <= curr:
                _, time, idx = heapq.heappop(heap)
                heapq.heappush(available, (time, idx))
            if available:
                time, idx = heapq.heappop(available)
                curr += time
                ans.append(idx)
            else:
                start, time, idx = heapq.heappop(heap)
                curr = start + time
                ans.append(idx)
        return ans
