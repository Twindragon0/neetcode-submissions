class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        self.memo = defaultdict(int)
        def recurse(lst):
            if tuple(lst) in self.memo:
                return self.memo[tuple(lst)]
            if not lst:
                return 0
            maxRes = 0
            for i in range(len(lst)):
                l = lst[i-1] if i-1 >= 0 else 1
                r = lst[i+1] if i+1 < len(lst) else 1
                m = lst.pop(i)
                maxRes = max(maxRes, l*r*m + recurse(lst))
                lst.insert(i, m)
            self.memo[tuple(lst)] = maxRes
            return maxRes
        return recurse(nums)