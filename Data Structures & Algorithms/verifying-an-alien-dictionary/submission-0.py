class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letterToPos = defaultdict(int)
        for i, char in enumerate(order):
            letterToPos[char] = i
        verified = [False] * (len(words)-1)
        maxLen = 0
        for word in words:
            maxLen = max(maxLen, len(word))
        for i in range(maxLen):
            for j in range(len(verified)):
                if not verified[j]:
                    if i < len(words[j]) and i >= len(words[j+1]):
                        return False
                    elif i >= len(words[j]):
                        verified[j] = True
                    elif letterToPos[words[j][i]] < letterToPos[words[j+1][i]]:
                        verified[j] = True
                    elif letterToPos[words[j][i]] > letterToPos[words[j+1][i]]:
                        return False
        return True