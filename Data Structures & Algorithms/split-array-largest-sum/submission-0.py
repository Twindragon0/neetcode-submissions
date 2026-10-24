class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = left
        while left <= right:
            mid = (left + right) // 2
            
            currSum = 0
            i = 0
            totalK = 0
            while i < len(nums):
                if currSum + nums[i] > mid:
                    totalK += 1
                    currSum = nums[i]
                else:
                    currSum += nums[i]
                i += 1
            totalK += 1
            
            if totalK == k:
                ans = mid
                right = mid - 1
            elif totalK > k:
                left = mid + 1
            else:
                right = mid - 1
        return ans
