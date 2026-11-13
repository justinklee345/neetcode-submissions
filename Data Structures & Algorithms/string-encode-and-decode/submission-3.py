class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)) + '#' + word)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        cnt = ""

        while i < len(s):
            if s[i] != '#':
                cnt += s[i]
                i += 1
            else:
                cnt = int(cnt)
                res.append(s[i + 1: i + cnt + 1])
                i += cnt + 1
                cnt = ""
        return res

            
        


