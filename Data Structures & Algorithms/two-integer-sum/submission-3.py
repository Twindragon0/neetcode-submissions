class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, num in enumerate(nums):
            if target - num in myMap:
                return [myMap[target - num], i]
            myMap[num] = i
        return [-1, -1]
            
        

        