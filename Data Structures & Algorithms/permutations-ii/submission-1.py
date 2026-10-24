class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        n = len(nums)
        def recurse(curr):
            if len(curr) == n:
                self.ans.append(curr.copy())
            else:
                i = 0
                while i < len(nums):
                    num = nums.pop(i)
                    curr.append(num)
                    recurse(curr)
                    curr.pop()
                    nums.insert(i, num)
                    while i+1 < len(nums) and nums[i] == nums[i+1]:
                        i += 1
                    i += 1
        recurse([])
        return self.ans