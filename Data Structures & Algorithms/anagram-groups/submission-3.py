from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            frequencies = defaultdict(int)
            for char in word:
                frequencies[char] += 1
            frequencies = sorted(frequencies.items())
            anagrams[tuple(frequencies)].append(word)
        ans = []
        for key, val in anagrams.items():
            ans.append(val)
        return ans

