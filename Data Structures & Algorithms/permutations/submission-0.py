class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recurse(subset, arr):
            if arr == []:
                self.ans.append(subset.copy())
            else:
                for i in range(len(arr)):
                    num = arr.pop(i)
                    subset.append(num)
                    recurse(subset, arr)
                    subset.pop(-1)
                    arr.insert(i, num)
        recurse([], nums)
        return self.ans