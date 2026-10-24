from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if counter == 0:
                candidate = nums[i]
                counter += 1
            elif candidate == nums[i]:
                counter += 1
            else:
                counter -= 1
        return candidate
            
        