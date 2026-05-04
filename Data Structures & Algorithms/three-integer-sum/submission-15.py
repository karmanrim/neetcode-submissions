class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -nums[i]
            l = 0
            r = len(nums) - 1
            while True:
                print([nums[l], nums[i], nums[r]])
                if r <= l:
                    break
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                if nums[r] + nums[l] > target:
                    r -= 1
                elif nums[r] + nums[l] < target:
                    l += 1
                else:
                    if sorted([nums[l], nums[i], nums[r]]) not in res:
                        res.append(sorted([nums[l], nums[i], nums[r]]))
                    l += 1
        return res