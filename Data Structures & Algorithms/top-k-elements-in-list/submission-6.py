class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 0
            res[num] += 1
        sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
        return [i[0] for i in sorted_res[:k]]