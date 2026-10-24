class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroP = -1
        oneP = -1
        twoP = -1
        for i in range(len(nums)):
            tmp = nums[i]
            twoP += 1
            nums[twoP] = 2
            if tmp == 1 or tmp == 0:
                oneP += 1
                nums[oneP] = 1
            if tmp == 0:
                zeroP += 1
                nums[zeroP] = 0
                
                

            



        
