class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x, y in points:
            dist = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(q, (dist, (x, y)))
        smallest = heapq.nsmallest(k, q)
        return [smallest[i][1] for i in range(len(smallest))]