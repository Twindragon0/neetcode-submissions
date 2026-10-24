class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, (-abs(x-num), -num))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted(-el[1] for el in heap)
