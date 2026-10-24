class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = []
        for idx, task in enumerate(tasks):
            arr.append((task[0], task[1], idx))
        arr.sort()
        ts = arr[0][0]
        available = []
        ans = []
        i = 0
        while i < len(arr) or available:
            while i < len(arr) and arr[i][0] <= ts:
                _, x, y = arr[i]
                i += 1
                heapq.heappush(available, (x, y))
            if i < len(arr) and not available:
                ts, x, y = arr[i]
                i += 1
                heapq.heappush(available, (x, y))
            processingTime, idx = heapq.heappop(available)
            ans.append(idx)
            ts += processingTime
        return ans