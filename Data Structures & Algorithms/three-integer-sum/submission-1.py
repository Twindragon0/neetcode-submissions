class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            mappings = set()
            for j in range(i+1, len(nums)):
                if -nums[i]-nums[j] in mappings:
                    ans.add(tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]])))
                mappings.add(nums[j])
        return list(ans)
