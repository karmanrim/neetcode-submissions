from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque([['', 0, 0]])
        print(q)
        while len(q[0][0]) < 2 * n:
            cur = q.popleft()
            if cur[2] < cur[1]:
                q.append([cur[0] + ')', cur[1], cur[2] + 1])
            if cur[1] < n:
                q.append([cur[0] + '(', cur[1] + 1, cur[2]])
        return [q[i][0] for i in range(len(q))]