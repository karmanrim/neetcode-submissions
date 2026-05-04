class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                j, h = stack.pop()
                max_area = max(max_area, h * (i - j))
                start = j

            stack.append([start, heights[i]])
        while stack:
            j, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - j))
        return max_area

            