class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum = [0] * (len(nums) + 1)
        prefixSum[0] = 0
        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        ans = 0
        for i in range(len(nums)):
            l = i
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if prefixSum[mid+1] - prefixSum[i] >= target:
                    ans = mid-i+1 if ans == 0 else min(ans, mid-i+1)
                    r = mid - 1
                else:
                    l = mid + 1
        return ans

        