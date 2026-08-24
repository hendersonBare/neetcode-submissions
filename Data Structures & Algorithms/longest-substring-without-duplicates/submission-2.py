class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        chars={}
        max_len=0
        while (l<=r and r<len(s)):
            #if we have seen the right character before we enter a while loop
            while s[r] in chars and l<r:
                del chars[s[l]]
                l+=1

            chars[s[r]] = 1
            r+=1
            max_len = max(max_len,(r-l))

        return max_len
