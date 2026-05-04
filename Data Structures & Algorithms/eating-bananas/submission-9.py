class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        min_k = max(piles)
        while r - l > 1:
            m = (r + l) // 2
            h_needed = 0
            for pile in piles:
                if pile % m == 0:
                    h_needed += pile // m
                else:
                    h_needed += pile // m + 1
            if h_needed <= h:
                min_k = min(min_k, m)
                r = m
            else:
                l = m
        return min_k

            