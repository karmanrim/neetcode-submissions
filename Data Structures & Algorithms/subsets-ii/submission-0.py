class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(i, cur):
            if i == len(nums):
                res.add(tuple(sorted(cur.copy())))
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)
            return
        dfs(0, [])
        return [list(r) for r in res]