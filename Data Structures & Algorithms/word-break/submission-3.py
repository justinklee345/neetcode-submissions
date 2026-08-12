class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canreach = [False for _ in range(len(s) + 1)]
        canreach[0] = True
        for i in range(len(s)):
            for word in wordDict:
                start_idx = i - len(word) + 1

                if start_idx >= 0 and canreach[start_idx] and s[start_idx: i + 1] == word:
                    canreach[i + 1] = True
                    break
        return canreach[-1]
            

'''
canreach[i] would refer to whether or not you can 
neetcode
01234567


penapple pen, penapple

'''

