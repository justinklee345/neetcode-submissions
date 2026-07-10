class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, best= 0, 0
        vocab = {}
        for r in range(0, len(s)):
            vocab[s[r]] = vocab.get(s[r], 0) + 1
            if (r - l + 1) - max(vocab.values()) <= k:
                best = max(best, r-l + 1)
            else:
                while (r - l + 1) - max(vocab.values()) > k:
                    vocab[s[l]] -= 1
                    l += 1
        
        return best
            