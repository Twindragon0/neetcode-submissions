class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valueToIdx = {}
        for i in range(len(nums)):
            if nums[i] in valueToIdx and i - valueToIdx[nums[i]] <= k:
                return True
            valueToIdx[nums[i]] = i
        return False


