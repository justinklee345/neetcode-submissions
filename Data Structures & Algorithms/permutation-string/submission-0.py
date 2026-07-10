class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        vocab = {}
        for letter in s1:
            vocab[letter] = vocab.get(letter, 0) + 1
        
        l = 0
        curr = {}
        for r in range(0, len(s2)):
            curr[s2[r]] = curr.get(s2[r], 0) + 1
            print(curr)

            if sum(curr.values()) == sum(vocab.values()):
                if curr == vocab:
                    print(curr.keys())
                    return True
                else:
                    if curr[s2[l]] == 1:
                        del curr[s2[l]]
                    else:
                        curr[s2[l]] -= 1
                    l += 1
        
        return False
            