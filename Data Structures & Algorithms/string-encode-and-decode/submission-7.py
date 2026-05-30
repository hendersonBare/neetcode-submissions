class Solution:

    def encode(self, strs: List[str]) -> str:
        full_str = ""
        for i in range(len(strs)):
            full_str += str(len(strs[i])) + "#" + strs[i]
        return full_str

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while(i < len(s)):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            ret.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return ret

