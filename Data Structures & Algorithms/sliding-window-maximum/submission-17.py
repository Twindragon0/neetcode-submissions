class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            maxSeen = nums[i]
            for j in range(i, i+k):
                maxSeen = max(maxSeen, nums[j])
            ans.append(maxSeen)
        return ans
        
