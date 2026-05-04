class Solution:
    def compare(self, ds: dict[str, int], dt: dict[str, int]) -> bool:
        for key, val in dt.items():
            if val > ds.get(key, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == '':
            return ''
        slow = 0
        min_len = len(s) + 1
        min_substring = ''
        ds, dt = {}, {}
        for c in t:
            dt[c] = 1 + dt.get(c, 0)
        slow = 0
        flag = False
        for i in range(len(s)):
            ds[s[i]] = 1 + ds.get(s[i], 0)
            while self.compare(ds, dt):
                ds[s[slow]] -= 1
                slow += 1
                flag = True
            if flag:
                slow -= 1
                ds[s[slow]] = 1 + ds.get(s[slow], 0)
                if i - slow + 1 < min_len:
                    min_len = i - slow + 1
                    min_substring = s[slow: i + 1]

        
        return min_substring 
