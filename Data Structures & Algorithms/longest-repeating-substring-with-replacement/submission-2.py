class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=l
        max_length=0
        c_arr=[0]*26
        while r < len(s):
            c_arr[ord(s[r])-65]+=1
            r+=1
            if r-l - max(c_arr) <= k:
                max_length = max(max_length, r-l)
            else:
                while r-l - max(c_arr) > k:
                    c_arr[ord(s[l])-65]-=1
                    l+=1
        return max_length