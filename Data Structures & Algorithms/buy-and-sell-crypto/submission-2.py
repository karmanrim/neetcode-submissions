class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        result = [-1] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] <= prices[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            if not stack or stack[-1] < prices[i]:
                stack.append(prices[i])
        for i in range(len(prices)):
            result[i] -= prices[i]
        return max(result) if max(result) > 0 else 0

        
            