class Solution:
    def isValid(self, s: str) -> bool:
        rules = {'{' : "}", "(": ")", "[": "]"}
        stack = []
        for c in s:
            if c in['{', "[", "("]:
                stack.append(c)
            if c in ['}', ']', ')']:
                if stack and rules[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0