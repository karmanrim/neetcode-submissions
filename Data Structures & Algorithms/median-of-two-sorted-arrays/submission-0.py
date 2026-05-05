class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(nums1) > len(nums2):
            A, B = B, A
        l = 0
        r = len(A) - 1
        while True:
            m = (l + r) // 2
            m_2 = half - m - 2
            Aleft = A[m] if m >= 0 else float('-infinity')
            Bleft = B[m_2] if m_2 >= 0 else float('-infinity')
            Aright = A[m + 1] if m + 1 < len(A) else float('infinity')
            Bright = B[m_2 + 1] if m_2 + 1 < len(B) else float('infinity')
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Bright, Aright)
                else:
                    return (max(Bleft, Aleft) + min(Bright, Aright)) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1





