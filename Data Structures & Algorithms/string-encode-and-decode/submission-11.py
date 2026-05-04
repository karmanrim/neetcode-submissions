class Solution:

    def encode(self, strs: List[str]) -> str:
        text = ""
        for word in strs:
            text = text + word + "\n"
        return text

    def decode(self, s: str) -> List[str]:
        word = ""
        res = []
        for char in s:
            if char == "\n":
                res.append(word)
                word = ""
                continue
            word += char
        return res