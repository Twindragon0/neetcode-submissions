class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = set()
        for i in range(len(nums)):
            first = nums[i]
            left = i+1
            right = len(nums)-1
            target = -first
            while left < right:
                if nums[left] + nums[right] == target:
                    self.ans.add(tuple([first, nums[left], nums[right]]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return list(self.ans)