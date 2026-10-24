class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        presents = [False] * len(nums)
        for num in nums:
            if 1 <= num <= len(nums):
                presents[num-1] = True
        for i in range(len(presents)):
            if presents[i] == False:
                return i+1
        return len(nums)+1


        
        
            
        