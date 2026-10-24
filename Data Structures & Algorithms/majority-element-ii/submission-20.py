class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        firstCan = 0
        firstCounter = 0
        secondCan = 0
        secondCounter = 0
        ans = []
        for num in nums:
            if firstCounter == 0:
                firstCounter += 1
                firstCan = num
            elif firstCan == num:
                firstCounter += 1
            elif secondCounter == 0:
                secondCounter += 1
                secondCan = num
            elif secondCan == num:
                secondCounter += 1
            else:
                firstCounter -= 1
                secondCounter -= 1
        cnt1 = cnt2 = 0
        for num in nums:
            if firstCan == num:
                cnt1 += 1
            if secondCan == num:
                cnt2 += 1
        if cnt1 > len(nums) // 3:
            ans.append(firstCan)
        if cnt2 > len(nums) // 3:
            ans.append(secondCan)
        return ans





