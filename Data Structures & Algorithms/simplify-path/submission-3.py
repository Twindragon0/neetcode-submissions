class Solution:
    def simplifyPath(self, path: str) -> str:
        new_els = []
        els = path.split("/")
        stk = []
        for el in els:
            if el == "." or el == "":
                continue
            elif el == "..":
                stk.pop() if stk else None
            else:
                stk.append(el)
        return "/" + "/".join(stk)