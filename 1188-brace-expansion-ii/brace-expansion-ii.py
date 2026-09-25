class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def combine(a, b):
            return {x + y for x in a for y in b}
        def parse(i):
            res = set()
            curr = {""}
            while i < len(expression) and expression[i] != '}':   
                if expression[i] == '{':
                    temp, i = parse(i + 1)
                    curr = combine(curr, temp)
                elif expression[i] == ',':
                    res |= curr
                    curr = {""}
                    i += 1
                else:
                    curr = combine(curr, {expression[i]})
                    i += 1
            res |= curr
            if i < len(expression) and expression[i] == '}':
                i += 1
            return res, i
        ans, _ = parse(0)
        return sorted(ans)