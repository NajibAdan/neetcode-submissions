class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        mid = (end + start) // 2
        if len(s) == 1: return True
        while start <= mid:
            # ignore non-alpha chars
            while start<len(s) and not(s[start].isalpha() or s[start].isdigit()):
                start +=1
            while end>0 and not (s[end].isalpha() or s[end].isdigit()):
                end -= 1
            if start>= len(s) or end<0: break
            if s[start].lower() != s[end].lower(): return False
            start += 1
            end -= 1
        return True