class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ans = self.permute(nums[1:])

        newAns = []
        for perm in ans:
            for i in range(len(perm)+1):
                permCopy = perm.copy()
                permCopy.insert(i, nums[0])
                newAns.append(permCopy)
        return newAns