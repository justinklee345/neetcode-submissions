class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vocab = set()
        cnt, maxcnt = 0, 0
        l = 0
        for r in range(len(s)):            
            while s[r] in vocab:
                cnt -= 1
                vocab.remove(s[l])
                l += 1
            
            cnt += 1
            maxcnt = max(maxcnt, cnt)
            vocab.add(s[r])
                
        return maxcnt