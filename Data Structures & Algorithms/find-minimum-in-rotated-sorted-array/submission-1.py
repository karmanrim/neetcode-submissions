class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while r - l > 1:
            m = (r + l) // 2
            if nums[m] > nums[0]:
                l = m
            else:
                r = m
        return nums[r] if r != len(nums) else nums[0]