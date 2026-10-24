class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        bins = [0] * (max(people)+1)
        for weight in people:
            bins[weight] += 1
        newPeople = []
        for i, num in enumerate(bins):
            while num != 0:
                newPeople.append(i)
                num -= 1
            
        left = 0
        right = len(newPeople) - 1
        boats = 0
        while left < right:
            if newPeople[left] + newPeople[right] > limit:
                right -= 1
                boats += 1
            else:
                left += 1
                right -= 1
                boats += 1
        if left == right:
            boats += 1
        return boats
