class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        longestStreak = 1
        currStreak = 1
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                currStreak += 1
                longestStreak = max(longestStreak, currStreak)
            elif nums[i-1] == nums[i]:
                continue
            else:
                currStreak = 1
        return longestStreak

            

