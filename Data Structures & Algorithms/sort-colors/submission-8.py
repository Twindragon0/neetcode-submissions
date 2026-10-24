class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroP, oneP, twoP = -1, -1, -1
        for i in range(len(nums)):
            prev = nums[i]
            twoP += 1
            nums[twoP] = 2
            if prev == 2:
                continue
            oneP += 1
            nums[oneP] = 1
            if prev == 1:
                continue
            zeroP += 1
            nums[zeroP] = 0
                

            



        
