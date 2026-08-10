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
        
        return list(groups.values())