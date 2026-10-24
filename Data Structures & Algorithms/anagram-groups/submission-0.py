from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            wordMap = {}
            for char in word:
                wordMap[char] = wordMap.get(char, 0) + 1
            key = tuple(sorted(wordMap.items()))
            ans[key].append(word)
        return list(ans.values())
        