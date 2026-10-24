class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroP = -1
        twoP = len(nums)
        i = 0
        while i < twoP:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0 and zeroP < i:
                zeroP += 1
                nums[i], nums[zeroP] = nums[zeroP], nums[i]
                if i == zeroP:
                    i += 1
            else:
                twoP -= 1
                nums[i], nums[twoP] = nums[twoP], nums[i]