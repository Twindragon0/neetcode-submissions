class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        nums.sort()
        def recurse(i, curr, lst):
            if curr < 0:
                return
            elif curr == 0:
                if tuple(lst) not in self.ans:
                    self.ans.add(tuple(lst.copy()))
            else:
                for j in range(i, len(nums)):
                    lst.append(nums[j])
                    recurse(j, curr-nums[j], lst)
                    recurse(j+1, curr-nums[j], lst)
                    lst.pop(-1)
        recurse(0, target, [])
        return [list(el) for el in self.ans]