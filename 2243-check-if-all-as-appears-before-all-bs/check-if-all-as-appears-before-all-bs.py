class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if i>0 and s[i] == 'a' and s[i-1] == 'b':
                return False
        return True