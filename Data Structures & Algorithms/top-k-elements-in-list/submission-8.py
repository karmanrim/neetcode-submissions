class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        freqs = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            freqs[freq].append(num)
        result = []
        for freq in freqs:
            for num in freq:
                result.append(num)
        return result[-k:]