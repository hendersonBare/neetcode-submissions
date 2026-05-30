class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        meta_map = {}
        for s in strs:
            clist = [0] * 26
            for c in s:
                clist[ord(c)-97] += 1
            ctuple = tuple(clist)
            if ctuple in meta_map:
                meta_map[ctuple].append(s)
            else:
                meta_map[ctuple] = [s]
        return list(meta_map.values())