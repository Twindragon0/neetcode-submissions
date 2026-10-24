class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        def recurse(i, currSubset):
            if len(currSubset) == k:
                self.ans.append(currSubset.copy())
            else:
                for j in range(i, n+1):
                    currSubset.append(j)
                    recurse(j+1, currSubset)
                    currSubset.pop()
        recurse(1, [])
        return self.ans