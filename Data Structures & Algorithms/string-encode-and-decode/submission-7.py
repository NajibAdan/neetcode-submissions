class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = '#'
        encoded_str = ''
        for word in strs:
            length = len(word)
            encoded_str += str(length) + sep + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        sep = "#"
        results = []
        i = j = 0
        while i < len(s):
            if s[j] == "#":
                word_length = int(s[i:j])
                results.append(s[j+1:j+1+word_length])
                j = j + word_length + 1
                i = j
            j += 1
        return results
