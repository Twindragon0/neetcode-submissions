class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        firstCan = 0
        firstCanCount = 0
        secondCan = 0
        secondCanCount = 0
        for num in nums:
            if firstCanCount == 0:
                firstCan = num
                firstCanCount += 1
            elif num == firstCan:
                firstCanCount += 1
            elif secondCanCount == 0:
                secondCan = num
                secondCanCount += 1
            elif num == secondCan:
                secondCanCount += 1
            else:
                firstCanCount -= 1
                secondCanCount -= 1
        ans = []
        cnt1 = cnt2 = 0
        for num in nums:
            if num == firstCan:
                cnt1 += 1
            if num == secondCan:
                cnt2 += 1
        if cnt1 > len(nums) // 3:
            ans.append(firstCan)
        if cnt2 > len(nums) // 3:
            ans.append(secondCan)
        return ans


