class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        ans = -1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans+1 if ans != len(nums)-1 and nums[ans+1] == target else -1

