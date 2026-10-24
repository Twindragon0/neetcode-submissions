class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        c = 0
        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                c -= heapq.heappop(heap)[1]
            c += trip[0]
            heapq.heappush(heap, (trip[2], trip[0]))
            if c > capacity:
                return False
        return True