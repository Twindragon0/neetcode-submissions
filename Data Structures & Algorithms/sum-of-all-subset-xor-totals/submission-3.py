class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def recurse(i, currSubset):
            toAdd = 0
            for el in currSubset:
                toAdd = toAdd ^ el
            self.ans += toAdd
            for j in range(i, len(nums)):
                currSubset.append(nums[j])
                recurse(j+1, currSubset)
                currSubset.pop()
        recurse(0, [])
        return self.ans

