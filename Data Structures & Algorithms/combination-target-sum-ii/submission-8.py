class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        def recurse(i, curr, currSum):
            if currSum == target:
                combinations.append(curr.copy())
            j = i
            while j < len(candidates):
                if currSum + candidates[j] > target:
                    break
                curr.append(candidates[j])
                recurse(j+1, curr, currSum+candidates[j])
                curr.pop(-1)
                while j+1 < len(candidates) and candidates[j] == candidates[j+1]:
                    j += 1
                j += 1
        recurse(0, [], 0)
        return combinations
