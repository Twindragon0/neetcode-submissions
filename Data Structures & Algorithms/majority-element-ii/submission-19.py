class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = set()
        nums = sorted(nums)

        currCandidate = 0
        currStreak = 0
        for num in nums:
            if currStreak == 0:
                currCandidate = num
                currStreak += 1
            elif currCandidate == num:
                currStreak += 1
            else:
                currStreak = 1
                currCandidate = num
            if currStreak > len(nums)//3:
                ans.add(currCandidate)
        return list(ans)



