from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies = defaultdict(int)
        target = len(nums) / 2
        for num in nums:
            frequencies[num] += 1
            if frequencies[num] >= target:
                return num
        