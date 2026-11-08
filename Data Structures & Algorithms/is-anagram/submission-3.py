class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}
        for i in range(len(s)):
            # s character frequency
            if s[i] in s_freq.keys():
                s_freq[s[i]] += 1
            else:
                s_freq[s[i]] = 1
            # t character frequency
            if t[i] in t_freq.keys():
                t_freq[t[i]] += 1
            else:
                t_freq[t[i]] = 1
        print (s_freq, t_freq)
        return s_freq == t_freq