class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bruteforce(nums, results, result):
            if len(nums) == 0:
                results.append(result.copy())
                return
            result.append(nums[0])    
            bruteforce(nums[1:], results, result)
            result.pop()
            bruteforce(nums[1:], results, result)
            return 

        results = []
        bruteforce(nums, results, [])
        return results