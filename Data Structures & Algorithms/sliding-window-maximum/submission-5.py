class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k-1):
            heapq.heappush(heap, -nums[i])
        unaccountedEls = set()
        ans = []
        for i in range(len(nums)-k+1):
            heapq.heappush(heap, -nums[i+k-1])
            while heap and heap[0] in unaccountedEls:
                unaccountedEls.remove(heap[0])
                heapq.heappop(heap)
            ans.append(-heap[0])
            unaccountedEls.add(-nums[i])
        return ans