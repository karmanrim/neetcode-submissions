class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_min_t = nums.copy()
        for i in range(len(nums)):
            if target < 0:
                nums[i] = -nums[i]
                n_min_t[i] = nums[i] + target
            else:
                n_min_t[i] = nums[i] - target
        if target < 0:
            target = abs(target)
        for i in range(len(n_min_t)):
            if n_min_t[i] > 0:
                continue
            abs_num = abs(n_min_t[i])
            if abs_num in nums:
                index = nums.index(abs_num)
                print(i, index, abs_num)
                if index == i:
                    try:
                        index = nums.index(abs_num, i+1)
                    except:
                        continue
                return sorted([i, index])
                
