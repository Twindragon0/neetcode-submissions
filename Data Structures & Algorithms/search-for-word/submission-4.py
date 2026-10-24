class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recurse(curr, visited, idx):
            if curr == "":
                return True
            elif not (0 <= idx[0] < len(board) and 0 <= idx[1] < len(board[0])):
                return False
            elif idx in visited:
                return False
            elif board[idx[0]][idx[1]] == curr[0]:
                visited.add(idx)
                ans = recurse(curr[1:], visited, (idx[0]+1, idx[1])) or recurse(curr[1:], visited, (idx[0], idx[1]+1)) or recurse(curr[1:], visited, (idx[0]-1, idx[1])) or recurse(curr[1:], visited, (idx[0], idx[1]-1))
                visited.remove(idx)
                return ans
            return False
        rows = len(board)
        cols = len(board[0])
        ans = False
        for i in range(rows * cols):
            if ans:
                break
            char = board[i // cols][i % cols]
            if char == word[0]:
                ans = ans or recurse(word, set(), (i // cols, i % cols))
        return ans
            



