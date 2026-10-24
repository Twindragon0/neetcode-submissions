class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                seenVals = set()
                for k in range(j+1, len(nums)):
                    if target-nums[i]-nums[j]-nums[k] in seenVals:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k], target-nums[i]-nums[j]-nums[k]])))
                    seenVals.add(nums[k])
        return list(ans)