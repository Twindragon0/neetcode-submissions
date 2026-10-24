class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            curr, val = queue.popleft()
            if curr == endWord:
                return val
            for word in wordList:
                if word in visited:
                    continue
                numDifferent = 0
                for i in range(min(len(word), len(curr))):
                    if word[i] != curr[i]:
                        numDifferent += 1
                if numDifferent == 1 and len(word) == len(curr):
                    queue.append((word, val+1))
                    visited.add(word)
        return 0