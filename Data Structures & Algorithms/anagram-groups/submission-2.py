class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_array_dic = {}
        for word in strs:
            char_array = ['0'] * 26
            for chr in word:
                curr_freq = int(char_array[ord(chr)-97])
                char_array[ord(chr)-97] = str(curr_freq + 1)
            char_array = ','.join(char_array)
            curr_set = str_array_dic.get(char_array,[])
            curr_set.append(word)
            str_array_dic[char_array] = curr_set
        # print(str_array_dic)
        return list(str_array_dic.values())
