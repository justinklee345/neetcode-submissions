class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, best = 0, 0
        vocab = set()
        for r in range(0, len(s)):
            print(vocab)
            if s[r] in vocab:
                
                while s[r] in vocab:
                    vocab.remove(s[l])
                    l += 1
                vocab.add(s[r])
            else:
                best = max(best, r - l + 1)
                vocab.add(s[r])
        return best
"""
zxyzxyz

0 0 1 """