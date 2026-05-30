class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        size = 1
        max_size = 1
        visited = {}
        while r < len(s):
            if (s[l] != s[r] and s[r] not in visited):
                visited[s[r]] = 1
                r+=1
                size+=1
                if size > max_size:
                    max_size = size
            elif (s[l] == s[r] or s[r] in visited):
                l+=1
                r = l + 1
                size = 1
                visited = {}
        return max_size
            