class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slidingWindow = deque(nums[0:k-1])
        ans = []
        for i in range(len(nums)-k+1):
            slidingWindow.append(nums[i+k-1])
            heap = []
            for el in slidingWindow:
                heapq.heappush(heap, -el)
            ans.append(-heap[0])
            slidingWindow.popleft()
        return ans