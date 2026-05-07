class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res
    
    def backtrack(self, perm, nums, is_picked):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return
        for i in range(len(nums)):
            if not is_picked[i]:
                perm.append(nums[i])
                is_picked[i] = True
                self.backtrack(perm, nums, is_picked)
                perm.pop()
                is_picked[i] = False
        