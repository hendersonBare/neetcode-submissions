class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res
    
    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            new_s = ""
            j+=1 #this is to skip the # character
            for k in range(j, j+length):
                new_s += s[k]
            strs.append(new_s)
            i=j+length
        return strs