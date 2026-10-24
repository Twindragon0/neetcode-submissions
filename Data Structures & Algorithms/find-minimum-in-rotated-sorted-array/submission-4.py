class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if nums[left] < nums[right]:
            return nums[0]
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid
            elif nums[left] == nums[mid]:
                left = mid+1
            else:
                right = mid
        print(left)
        print(right)
        return nums[(left) % len(nums)]