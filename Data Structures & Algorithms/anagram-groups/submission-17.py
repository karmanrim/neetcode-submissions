class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            cur_map = [0] * 26
            for char in word:
                cur_map[ord(char) - ord('a')] += 1
            key = tuple(cur_map)
            if key not in result:
                result[key] = []
            result[key].append(word)
        return [result[key] for key in result]
