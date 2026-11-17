class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        vocab = {}
        maxf = 0
        res = 0

        l = 0
        for r in range(len(s)):
            vocab[s[r]] = vocab.get(s[r], 0) + 1
            maxf = max(vocab[s[r]], maxf)

            while r - l + 1 - maxf > k:
                vocab[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
