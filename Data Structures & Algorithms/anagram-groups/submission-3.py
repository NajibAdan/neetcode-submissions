class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_arr = []
        freq_map = {}
        pos = 0
        for string in strs:
            freq = [0] * 26
            for chr in string:
                freq[ord(chr)-97] += 1
            freq = tuple(freq)
            if freq in freq_map:
                result_arr[freq_map[freq]].append(string)
            else:
                result_arr.append([string])
                freq_map[freq] = pos
                pos += 1
        return result_arr