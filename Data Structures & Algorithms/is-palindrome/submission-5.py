class Solution:
    def checkAlphanumeric(self, s: str)-> bool:
        ascii_value = ord(s)
        if (ascii_value >= ord('0') and ascii_value <= ord('9')) or (ascii_value >= ord('A') and ascii_value <= ord('z')):
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while back > front:
            while not self.checkAlphanumeric(s[back]) and back > front:
                back -= 1
            while not self.checkAlphanumeric(s[front]) and back > front:
                front += 1
            if s[front].lower() == s[back].lower():
                front += 1
                back -= 1
            else:
                return False
        return True
                