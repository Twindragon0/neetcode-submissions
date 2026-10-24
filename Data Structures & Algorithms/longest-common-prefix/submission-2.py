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
    
    def lcp(self, word, prefixLen):
        curr = self.root
        i = 0
        for char in word:
            if char not in curr.children:
                return min(prefixLen, i)
            i += 1
            curr = curr.children[char] 
        return min(prefixLen, i)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        myTrie = Trie()
        myTrie.insert(strs[0])
        prefixLength = len(strs[0])
        for word in strs:
            prefixLength = myTrie.lcp(word, prefixLength)
        return strs[0][:prefixLength]
        
        