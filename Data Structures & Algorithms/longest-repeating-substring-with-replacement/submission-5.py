class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        vocab = [0 for _ in range(26)]
        l = 0
        for r in range(len(s)):
            vocab[ord(s[r]) - ord('A')] += 1

            while sum(sorted(vocab)[:-1]) > k:
                vocab[ord(s[l]) - ord('A')] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen

'''
XYYX

[1, ]
'''