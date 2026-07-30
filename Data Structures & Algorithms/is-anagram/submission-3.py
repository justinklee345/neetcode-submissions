class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem = {}
        for c in s:
            mem[c] = mem.get(c, 0) + 1
        
        for c in t:
            mem[c] = mem.get(c, 0) - 1
        
        for k in mem.keys():
            if mem[k] != 0:
                return False
        return True