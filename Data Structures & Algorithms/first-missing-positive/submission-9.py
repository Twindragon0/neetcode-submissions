class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [False] * len(nums)
        for num in nums:
            if 1 <= num <= len(nums):
                arr[num-1] = True
        for i in range(len(arr)):
            if arr[i] == False:
                return i+1
        return len(arr)+1
        
        
            
        