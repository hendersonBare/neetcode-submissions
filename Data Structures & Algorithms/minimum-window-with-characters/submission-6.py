class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""

        countT,window = {},{}
        need,have = 0,0
        
        for c in t:
            countT[c] = countT.get(c,0)+1

        need = len(countT)
        res, resLen = [-1,-1], float("infinity")
        l=0

        for r in range(0,len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            if c in countT and window[c]==countT[c]:
                have+=1

            while have==need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                
                z = s[l]
                window[z] -= 1
                if z in countT and window[z] < countT[z]:
                    have-=1
                l+=1
        
        if resLen < float("infinity"):
            l,r = res[0],res[1]
            return s[l:r+1]
        return ""
