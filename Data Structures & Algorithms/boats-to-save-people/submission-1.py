class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left = 0
        right = len(people) - 1
        boats = 0
        while left < right:
            if people[left] + people[right] > limit:
                right -= 1
                boats += 1
            else:
                left += 1
                right -= 1
                boats += 1
        if left == right:
            boats += 1
        return boats
