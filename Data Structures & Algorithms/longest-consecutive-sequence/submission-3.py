class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        longestStreak = 0
        for num in nums:
            mySet.add(num)
        for num in nums:
            if num-1 in mySet:
                continue
            else:
                currStreak = 0
                currNum = num
                while currNum in mySet:
                    currStreak += 1
                    currNum += 1
                longestStreak = max(longestStreak, currStreak)
        return longestStreak
            

