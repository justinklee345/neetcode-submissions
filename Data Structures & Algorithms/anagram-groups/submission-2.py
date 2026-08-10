class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            vocab = [0 for _ in range(26)]
            for charac in word:
                vocab[ord(charac) - ord('a')] += 1
            
            key = str(vocab)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        res = []
        for group in groups.keys():
            inner = []
            for word in groups[group]:
                inner.append(word)
            res.append(inner)
        return res