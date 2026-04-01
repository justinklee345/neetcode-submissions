class Solution:

    def encode(self, strs: List[str]) -> str:
        retstr = ""
        for (i, s) in enumerate(strs):
            retstr += str(len(s)) + "#" + s
        print("encoded: ", retstr)
        return retstr

    def decode(self, s: str) -> List[str]:
        retlst = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            retlst.append(s[i: i + length])
            i = i + length 

        print("decoded", retlst)
        return retlst
