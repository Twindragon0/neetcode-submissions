class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = set()
        def recurse(i, curr, lst):
            if curr == target:
                self.ans.add(tuple(lst.copy()))
            elif curr > target or i >= len(candidates):
                return
            else:
                lst.append(candidates[i])
                recurse(i+1, curr+candidates[i], lst)
                lst.pop(-1)
                while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                    i += 1
                recurse(i+1, curr, lst)
        recurse(0, 0, [])
        return [list(el) for el in self.ans]
