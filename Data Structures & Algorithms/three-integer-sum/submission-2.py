class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left += 1
                else:
                    ans.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
        return list(ans)
