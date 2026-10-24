class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeros = 0
        numOnes = 0
        numTwos = 0
        for num in nums:
            if num == 0:
                numZeros += 1
            elif num == 1:
                numOnes += 1
            else:
                numTwos += 1
        for i in range(len(nums)):
            if numZeros != 0:
                numZeros -= 1
                nums[i] = 0
            elif numOnes != 0:
                numOnes -= 1
                nums[i] = 1
            else:
                numTwos -= 1
                nums[i] = 2
                
                

            



        
