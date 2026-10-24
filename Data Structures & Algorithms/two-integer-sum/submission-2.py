class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newNums = []
        for i, num in enumerate(nums):
            newNums.append([num, i])
        newNums = sorted(newNums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if newNums[left][0] + newNums[right][0] < target:
                left += 1
            elif newNums[left][0] + newNums[right][0] > target:
                right -= 1
            else:
                return sorted([newNums[left][1], newNums[right][1]])
        return [-1, -1]
            
        

        