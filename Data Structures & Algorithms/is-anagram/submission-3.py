class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            t = t.replace(s[i], "", 1)
        if len(t) == 0:
            return True
        else:
            return False