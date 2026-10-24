class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            mySet.add(num)
        longestSequence = 0
        for num in nums:
            if num-1 not in mySet:
                currStreak = 0
                currNum = num
                while currNum in mySet:
                    currStreak += 1
                    currNum = currNum + 1
                longestSequence = max(longestSequence, currStreak)
        return longestSequence


            

