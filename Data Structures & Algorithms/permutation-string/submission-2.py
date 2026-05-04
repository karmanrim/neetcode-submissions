class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = [0] * 26
        counter_s2 = [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            counter_s1[ord(s1[i]) - ord('a')] += 1
            counter_s2[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s1), len(s2)):
            if counter_s1 == counter_s2:
                return True
            counter_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            counter_s2[ord(s2[i]) - ord('a')] += 1
        return counter_s1 == counter_s2