class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(lo, hi):
            if lo > hi:
                return -1
            mid = (lo+hi) // 2
            if nums[mid] > target:
                return recurse(lo, mid-1)
            elif nums[mid] < target:
                return recurse(mid+1, hi)
            else:
                return mid
        return recurse(0, len(nums)-1)