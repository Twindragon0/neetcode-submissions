class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        def recurse(curr):
            if len(curr) == n:
                self.ans.append(curr.copy())
            else:
                for i in range(len(nums)):
                    num = nums.pop(i)
                    curr.append(num)
                    recurse(curr)
                    curr.pop()
                    nums.insert(i, num)
        recurse([])
        return self.ans

        


