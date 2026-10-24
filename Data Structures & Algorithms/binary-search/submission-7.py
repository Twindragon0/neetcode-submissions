class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the first index that is > target, and then return 1 before that
        l = 0
        r = len(nums)-1
        ans = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else: # nums[mid] > target
                ans = mid
                r = mid - 1
        return ans-1 if nums[ans-1] == target else -1
        

