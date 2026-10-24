class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            first = nums[i]
            mappings = set()
            for j in range(i+1, len(nums)):
                if -first - nums[j] in mappings:
                    ans.add(tuple(sorted([first, nums[j], -first-nums[j]])))
                mappings.add(nums[j])
        return list(ans)