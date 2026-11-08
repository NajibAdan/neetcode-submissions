class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += f"{len(x)}#{x}"
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        x = 0        
        while x < len(s):
            y = 0
            while s[x+1+y] != '#':
                y+=1
            print(s[x:x+y+1])
            length = int(s[x: x +1 + y])
            start = x+2+y
            word = s[start:start+length]
            print(word)
            res.append(word)
            x = x+2 + y +length
        return res
