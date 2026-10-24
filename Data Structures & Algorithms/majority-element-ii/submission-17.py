class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = set()
        nums = sorted(nums)

        currStreak = 0
        currCand = 0
        for num in nums:
            if currStreak == 0:
                currStreak += 1
                currCand = num
            elif num == currCand:
                currStreak += 1
            else:
                currStreak = 1
                currCand = num
            if currStreak > len(nums)//3:
                ans.add(currCand)
        return list(ans)


