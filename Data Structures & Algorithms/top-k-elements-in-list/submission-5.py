class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        heap = []
        for (num, freq) in frequencies.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
