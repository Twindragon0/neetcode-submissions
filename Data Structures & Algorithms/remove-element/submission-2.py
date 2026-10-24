class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = [] # all nums that arent val
        for num in nums:
            if num != val:
                tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
        