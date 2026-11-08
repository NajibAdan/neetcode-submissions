class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += f"{len(word)}|{word}"
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        print(s)
        while i < len(s):
            j = i
            # loop through until we find our seperator
            while j < len(s) and s[j] != '|' :
                j += 1
            # length of the word is from i to j
            print(f"i: {i} and j: {j}")
            print(f"Length: {s[i: j]}")
            length = int(s[i: j])
            start_pos = j + 1
            word = s[start_pos: start_pos+length]
            print(word)
            result.append(word)
            i = j + length + 1
        return result