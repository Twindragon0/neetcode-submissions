class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        # run it on nums[2:-1] and nums[1:]]
        dp1 = [0] * len(nums[2:-1])
        dp1[0] = nums[2]
        for i in range(3, len(nums)-1):
            dp1[i-2] = max(dp1[i-3], dp1[i-4] + nums[i])
        dp2 = [0] * len(nums[1:])
        dp2[0] = nums[1]
        for i in range(2, len(nums)):
            dp2[i-1] = max(dp2[i-2], dp2[i-3] + nums[i])
        return max(dp1[-1]+nums[0], dp2[-1])
