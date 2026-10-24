class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nextWrite = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
                continue
            else:
                nums[nextWrite] = nums[i]
                nextWrite += 1
                i += 1
        return nextWrite
        