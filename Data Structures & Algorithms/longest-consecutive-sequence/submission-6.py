class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longestSequence = 1
        currSequence = 1
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                currSequence += 1
                longestSequence = max(longestSequence, currSequence)
            elif nums[i] == nums[i-1]:
                continue
            else:
                currSequence = 1
        return longestSequence


            

