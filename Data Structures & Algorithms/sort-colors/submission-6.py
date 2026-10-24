class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        endZeros = -1
        startTwos = len(nums)
        i = 0
        while i < startTwos:
            if nums[i] == 0:
                endZeros += 1
                nums[i], nums[endZeros] = nums[endZeros], nums[i]
            elif nums[i] == 2:
                startTwos -= 1
                nums[i], nums[startTwos] = nums[startTwos], nums[i]
            if nums[i] == 1 or i <= endZeros:
                i += 1
                
                

            



        
