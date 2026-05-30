class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        chars = {}
        curr_len = 0
        while (l<=r and r<len(s)):
            if (s[r] not in chars):
                chars[s[r]] = 1
                curr_len += 1
                r+=1
                if curr_len > max_len:
                    max_len = curr_len
            else:
                del chars[s[l]]
                l+=1
                curr_len-=1
        return max_len