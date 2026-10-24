class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if left == right:
                return boats+1
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                right -= 1
                boats += 1
        return boats
