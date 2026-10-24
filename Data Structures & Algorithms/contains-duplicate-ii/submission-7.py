class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        i = 0
        while i <= min(k, len(nums)-1):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            i += 1
        for i in range(k+1, len(nums)):
            seen.remove(nums[i-k-1])
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        


