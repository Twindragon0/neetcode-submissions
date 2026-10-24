class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # INVARIANT: at the beginning of an iteration, we haven't seen
        #            a value that appears more than once
        uniqueVals = set()
        for num in nums:
            if num in uniqueVals:
                return True
            uniqueVals.add(num)
        return False
        