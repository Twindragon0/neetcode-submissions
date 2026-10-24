class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = -1
        while left <= right:
            capacity = (left + right) // 2

            totalDays = 0
            i = 0
            currCapacity = 0
            while i < len(weights):
                if weights[i] + currCapacity > capacity:
                    totalDays += 1
                    currCapacity = weights[i]
                else:
                    currCapacity += weights[i]
                i += 1
            totalDays += 1
            
            if totalDays > days:
                left = capacity + 1
            else:
                ans = capacity
                right = capacity - 1
        return ans

