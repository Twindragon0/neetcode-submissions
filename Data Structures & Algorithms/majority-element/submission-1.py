from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        counter = 1
        for i in range(len(nums)):
            if counter == 0:
                candidate = nums[i]
                counter += 1
            elif nums[i] == candidate:
                counter += 1
            else:
                counter -= 1
        return candidate
            
        