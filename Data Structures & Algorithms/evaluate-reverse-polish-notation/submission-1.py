class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        rules = {
            '+': lambda x1, x2: x1 + x2,
            '-': lambda x1, x2: x1 - x2,
            '*': lambda x1, x2: x1 * x2,
            '/': lambda x1, x2: int(float(x1) / x2),
        }
        for c in tokens:
            if c in rules:
                term2 = stack.pop()
                term1 = stack.pop()
                stack.append(rules[c](term1, term2))
                continue
            stack.append(int(c))
        return stack[0]