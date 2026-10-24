class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        def recurse(i, subset):
            if len(subset) == k:
                self.ans.append(subset.copy())
            else:
                for j in range(i, n+1):
                    subset.append(j)
                    recurse(j+1, subset)
                    subset.pop(-1)
        recurse(1, [])
        return self.ans