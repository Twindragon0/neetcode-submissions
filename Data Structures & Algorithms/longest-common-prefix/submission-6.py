class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
    
    def lcp(self, word):
        prefixLength = 0
        curr = self.root
        for char in word:
            if char not in curr.children:
                return prefixLength
            prefixLength += 1
            curr = curr.children[char]
        return prefixLength


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        myTrie = Trie()
        myTrie.insert(strs[0])
        prefixLength = len(strs[0])
        for word in strs:
            prefixLength = min(prefixLength, myTrie.lcp(word))
        return strs[0][:prefixLength]
        

        
        