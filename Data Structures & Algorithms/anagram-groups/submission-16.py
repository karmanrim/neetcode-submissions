class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char) - ord("a")] += 1
            key = tuple(counter)
            if key not in res:
                res[key] = []
            res[key].append(word)
        return list(res.values())

