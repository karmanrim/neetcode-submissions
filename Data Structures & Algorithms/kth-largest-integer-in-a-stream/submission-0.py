import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        heapq.heapify(self.q)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        return heapq.nlargest(self.k, self.q)[-1]
