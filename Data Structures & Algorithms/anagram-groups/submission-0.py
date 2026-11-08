class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for string in strs:
            temp = ''.join(sorted(string)) 
            if temp in hashMap: hashMap[temp].append(string)
            else: hashMap[temp] = [string]
        result = []
        for key in hashMap:
            result.append(hashMap[key])
        return result