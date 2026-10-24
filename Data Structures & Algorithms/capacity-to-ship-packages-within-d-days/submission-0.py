class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = 1
        while left <= right:
            totalCapacity = (left + right) // 2

            currCapacity = 0
            totalDays = 0
            i = 0
            while i < len(weights):
                if weights[i] + currCapacity > totalCapacity:
                    totalDays += 1
                    currCapacity = weights[i]
                else:
                    currCapacity += weights[i]
                i += 1
            totalDays += 1
            if totalDays <= days:
                ans = totalCapacity
                right = totalCapacity - 1
            else:
                left = totalCapacity + 1
        return ans
