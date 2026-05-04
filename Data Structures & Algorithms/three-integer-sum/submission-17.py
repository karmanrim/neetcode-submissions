class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            p1, p2 = 0, len(nums) - 1
            target = -nums[i]
            while p2 > p1:
                if nums[p2] + nums[p1] > target:
                    p2 -= 1
                    continue
                if nums[p2] + nums[p1] < target:
                    p1 += 1
                    continue
                if nums[p2] + nums[p1] == target:
                    if p1 != i and p2 != i:
                        result.add(tuple(sorted([nums[p1],nums[p2], nums[i]])))
                    p1 += 1
                    p2 -= 1
        return list(result)