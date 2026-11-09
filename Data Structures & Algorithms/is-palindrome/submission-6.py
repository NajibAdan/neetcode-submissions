class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        i = 0
        j = length - 1
        while i < j:
            comp_a = s[i]
            comp_b = s[j]
            if (comp_a.isalpha() or comp_a.isdigit()) and (comp_b.isalpha() or comp_b.isdigit()):
                if comp_a.lower() == comp_b.lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif not(comp_a.isalpha() or comp_a.isdigit()):
                i += 1
            elif not(comp_b.isalpha() or comp_b.isdigit()):
                j -= 1
        return True

            