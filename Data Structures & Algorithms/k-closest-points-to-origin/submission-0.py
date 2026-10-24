class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []
        for point in points:
            heapq.heappush(heap, (math.sqrt(point[0]**2 + point[1]**2), point))
            if len(heap) > len(points)-k:
                distance, el = heapq.heappop(heap)
                ans.append(el)
        return ans