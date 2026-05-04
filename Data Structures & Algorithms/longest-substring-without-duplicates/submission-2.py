class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_chars = set()
        max_length = 0
        length = 0
        slow, fast = 0, 0
        while fast < len(s):
            print(cur_chars)
            if s[fast] in cur_chars:
                while s[slow] != s[fast]:
                    cur_chars.remove(s[slow])
                    slow += 1
                slow += 1
                max_length = max(length, max_length)
                length = fast - slow
            cur_chars.add(s[fast])
            length += 1
            fast += 1
        max_length = max(length, max_length)
        return max_length 