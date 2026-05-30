class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            while not self.isAlphaNum(s[p1]) and p1 < p2:
                p1 += 1
            while not self.isAlphaNum(s[p2]) and p1 < p2:
                p2 -= 1
            if s[p1].lower() != s[p2].lower():
                return False
            p1+=1
            p2-=1
        return True

    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))