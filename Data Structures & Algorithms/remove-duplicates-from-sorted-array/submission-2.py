class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = sorted(set(nums))
        nums[:len(mySet)] = list(mySet)
        return len(mySet)

