class Solution:
    def longestPalindrome(self, s: str) -> str:
        #s is always atleast len 1
        #the way we can find all substrings
        #is by iterating through the string
        #and expanding outwards from each character, with
        #that character as the center of the palindrome
        #need to ensure that we consider both odd length
        #and even length palindromes
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd palindromes
            l=r=i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            #even palindromes
            l,r=i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res