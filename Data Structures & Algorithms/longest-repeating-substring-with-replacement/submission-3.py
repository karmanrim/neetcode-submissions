class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = -1
        result = 0
        letter_count = [0] * 26
        while l < len(s):
            cur_letter_count = sum(letter_count) - max(letter_count)

            while r + 1 < len(s) and (cur_letter_count <= k):
                print(letter_count)
                r += 1
                letter_count[ord(s[r]) - ord('A')] += 1
                cur_letter_count = sum(letter_count) - max(letter_count)
            print(letter_count)
            if cur_letter_count > k:
                result = max(result, sum(letter_count) - 1)
            else:
                result = max(result, sum(letter_count))
            letter_count[ord(s[l]) - ord('A')] -= 1
            cur_letter_count = sum(letter_count) - max(letter_count)
            print(letter_count)
            l += 1
        return result