class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] < target:
                return recurse(mid+1, r)
            elif nums[mid] > target:
                return recurse(l, mid-1)
            else:
                return mid
        return recurse(0, len(nums)-1)
        

