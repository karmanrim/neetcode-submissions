class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) 
        while r - l > 1:
            m = (r + l) // 2
            if nums[m] > nums[0]:
                l = m
            else:
                r = m 
        rotate = r
        l = rotate
        r = rotate + len(nums)
        while r - l > 1:
            m = (r + l) // 2
            if nums[m % len(nums)] <= target:
                l = m
            else:
                r = m
        return l % len(nums) if nums[l % len(nums)] == target else -1 
