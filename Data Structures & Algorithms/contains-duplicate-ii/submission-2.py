class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vals = set()
        for i in range(min((k+1), len(nums))):
            if nums[i] in vals:
                return True
            vals.add(nums[i])
        for j in range(k+1, len(nums)):
            vals.remove(nums[j-k-1])
            if nums[j] in vals:
                return True
            vals.add(nums[j])
        return False