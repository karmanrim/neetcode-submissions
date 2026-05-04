class Solution:

    def encode(self, strs: List[str]) -> str:
        prev_str = ""
        for word in strs:
            prev_str = prev_str + word + "\n"
        return prev_str

    def decode(self, s: str) -> List[str]:
        return s.split("\n")[:-1]