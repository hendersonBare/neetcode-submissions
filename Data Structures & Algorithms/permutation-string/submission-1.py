class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map = {}
        s2_map = {}
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c,0)
        
        l = 0
        s2_map[s2[0]] = 1
        if s2_map == s1_map:
            return True
        for r in range(1, len(s2)):
            s2_map[s2[r]] = 1 + s2_map.get(s2[r],0)
            if r - l+1 == len(s1) and s1_map == s2_map:
                return True
            elif r-l+1 == len(s1) and s1_map != s2_map:
                print(l, r)
                print(s1_map)
                print(s2_map)
                if s2_map[s2[l]] == 1:
                    s2_map.pop(s2[l])
                else:
                    s2_map[s2[l]] -= 1
                l +=1
        return False