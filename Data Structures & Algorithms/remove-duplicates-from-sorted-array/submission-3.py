class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        toWrite = 1
        curr = 1
        prev = nums[0]
        while curr < len(nums):
            if nums[curr] == prev:
                curr += 1
            else:
                nums[toWrite] = nums[curr]
                prev = nums[curr]
                curr += 1
                toWrite += 1
        return toWrite


