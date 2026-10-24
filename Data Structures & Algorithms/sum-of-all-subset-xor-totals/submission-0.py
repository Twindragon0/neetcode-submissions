class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def recurse(i, curr):
            if i == len(nums):
                xorTotal = 0
                for num in curr:
                    xorTotal ^= num
                self.ans += xorTotal
            else:
                curr.append(nums[i])
                recurse(i+1, curr)
                curr.pop(-1)
                recurse(i+1, curr)
        recurse(0, [])
        return self.ans