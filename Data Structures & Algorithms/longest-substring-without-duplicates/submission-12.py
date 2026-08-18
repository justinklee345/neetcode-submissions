class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vocab = set()
        maxcnt = 0
        l = 0
        for r in range(len(s)):            
            while s[r] in vocab:
                vocab.remove(s[l])
                l += 1
            
            maxcnt = max(maxcnt, r - l + 1)
            vocab.add(s[r])
                
        return maxcnt