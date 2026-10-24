class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowSet = set()
        j = 0
        while j <= k:
            if j == len(nums):
                return False
            if nums[j] in windowSet:
                return True
            windowSet.add(nums[j])
            j += 1
        for i in range(k+1, len(nums)):
            windowSet.remove(nums[i-k-1])
            if nums[i] in windowSet:
                return True
            windowSet.add(nums[i])
        return False

