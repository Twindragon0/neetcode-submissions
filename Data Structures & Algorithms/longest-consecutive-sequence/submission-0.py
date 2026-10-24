class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streaks = defaultdict(list) # (start, end)
        maxStreak = 0
        for num in nums:
            if num not in streaks:
                if num+1 in streaks and num-1 not in streaks:
                    streaks[num] = [num, streaks[num+1][1]]
                    streaks[streaks[num+1][1]] = [num, streaks[num+1][1]]
                    maxStreak = max(maxStreak, streaks[num+1][1] - num + 1)
                elif num-1 in streaks and num+1 not in streaks:
                    streaks[num] = [streaks[num-1][0], num]
                    streaks[streaks[num-1][0]] = [streaks[num-1][0], num]
                    maxStreak = max(maxStreak, num - streaks[num-1][0] + 1)
                elif num-1 in streaks and num+1 in streaks:
                    streaks[streaks[num-1][0]][1] = streaks[num+1][1]
                    streaks[streaks[num+1][1]][0] = streaks[num-1][0]
                    maxStreak = max(maxStreak, streaks[num+1][1] - streaks[num-1][0] + 1)
                else:
                    streaks[num] = [num, num]
                    maxStreak = max(maxStreak, 1)
                
        return maxStreak
