class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def bruteforce(nums, results, result, target, cur_sum):
            if cur_sum > target or len(nums) == 0:
                return 
            if cur_sum == target:
                results.add(tuple(result.copy()))
                return 
            result.append(nums[0])
            cur_sum += nums[0]
            bruteforce(nums, results, result, target, cur_sum)
            bruteforce(nums[1:], results, result, target, cur_sum)
            cur_sum -= nums[0]
            result.pop()
            bruteforce(nums[1:], results, result, target, cur_sum)
            return

        results = set()
        bruteforce(nums, results, [], target, 0)
        return [list(result) for result in results ]

