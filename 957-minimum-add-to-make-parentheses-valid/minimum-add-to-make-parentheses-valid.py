class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if c =="(":
                stack.append(c)
            else:
                if stack and stack[-1]=='(':
                    stack.pop(-1)
                else:
                    stack.append(c)
        return len(stack)
