class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            if num > 0:
                numsSet.add(num)
        for i in range(1, len(nums)+1):
            if i not in numsSet:
                return i
        return len(nums)+1
            
        