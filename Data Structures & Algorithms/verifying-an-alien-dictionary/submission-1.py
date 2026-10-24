class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        verified = [False] * (len(words)-1)
        letterToPos = defaultdict(int)
        for i, letter in enumerate(order):
            letterToPos[letter] = i
        maxLen = 0
        for word in words:
            maxLen = max(maxLen, len(word))
        for i in range(maxLen):
            for j in range(len(verified)):
                if not verified[j]:
                    if i >= len(words[j]):
                        verified[j] = True
                    elif i >= len(words[j+1]):
                        return False
                    elif letterToPos[words[j][i]] < letterToPos[words[j+1][i]]:
                        verified[j] = True
                    elif letterToPos[words[j][i]] > letterToPos[words[j+1][i]]:
                        return False
                    print(i)
                    print(j)
                    print(verified)
        return True