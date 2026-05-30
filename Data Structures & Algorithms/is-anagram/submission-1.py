class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = [0]*26
        t_set = [0]*26

        for c in s:
            s_set[ord(c) - 97] += 1

        for c in t:
            t_set[ord(c) - 97] += 1

        return s_set == t_set