class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        endZero = -1
        startTwo = len(nums)
        i = 0
        while i < startTwo:
            if nums[i] == 0:
                endZero += 1
                nums[endZero], nums[i] = nums[i], nums[endZero]
            elif nums[i] == 2:
                startTwo -= 1
                nums[startTwo], nums[i] = nums[i], nums[startTwo]
            if i <= endZero or i >= startTwo or nums[i] == 1:
                i += 1
            



        
