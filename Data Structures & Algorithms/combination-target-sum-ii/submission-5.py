class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        def recurse(i, currSubset):
            if sum(currSubset) == target:
                self.ans.append(currSubset.copy())
            else:
                j = i
                while j < len(candidates):
                    if sum(currSubset) + candidates[j] > target:
                        break
                    currSubset.append(candidates[j])
                    recurse(j+1, currSubset)
                    currSubset.pop()
                    while j+1 < len(candidates) and candidates[j] == candidates[j+1]:
                        j += 1
                    j += 1
        recurse(0, [])
        return self.ans
