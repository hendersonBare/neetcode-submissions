class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = ""
        for s in strs:
            ret_str += str(len(s))
            ret_str += "#"
            ret_str += s
        return ret_str

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        i = 0
        j = 0
        ret_arr = []
        while j < len(s):
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            new_str = s[j+1:j+size+1]
            ret_arr.append(new_str)
            i = j+size+1
            j=i
        return ret_arr