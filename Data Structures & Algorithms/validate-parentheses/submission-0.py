class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) > 1:
                if stack[-2] == '{' and stack[-1] == '}':
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '(' and stack[-1] == ')':
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '[' and stack[-1] == ']':
                    stack.pop()
                    stack.pop()
        return not bool(stack)