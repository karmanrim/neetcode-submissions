class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeros = 0
        prev_prod = [1]
        for num in nums:
            if num == 0:
                count_zeros += 1
                prev_prod.append(prev_prod[-1])
                continue
            prev_prod.append(prev_prod[-1] * num)
        result = []
        for num in nums:
            if count_zeros > 1:
                result.append(0)
            elif count_zeros == 1:
                result.append(prev_prod[-1]) if num == 0 else result.append(0)
            else:
                result.append(prev_prod[-1] // num)
        return result
        