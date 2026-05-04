from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []
        if k >= len(nums):
            return [max(nums)]
        for i in range(k):
            window.append(nums[i])
        result.append(max(window))
        for i in range(k, len(nums)):
            window.popleft()
            window.append(nums[i])
            result.append(max(window))
        return result
