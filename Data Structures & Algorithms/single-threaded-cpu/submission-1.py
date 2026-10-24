class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        for idx, task in enumerate(tasks):
            heapq.heappush(heap, (task[0], task[1], idx))
        ts = heap[0][0]
        available = []
        ans = []
        while heap or available:
            while heap and heap[0][0] <= ts:
                _, x, y = heapq.heappop(heap)
                heapq.heappush(available, (x, y))
            if heap and not available:
                ts, x, y = heapq.heappop(heap)
                heapq.heappush(available, (x, y))
            processingTime, idx = heapq.heappop(available)
            ans.append(idx)
            ts += processingTime
        return ans