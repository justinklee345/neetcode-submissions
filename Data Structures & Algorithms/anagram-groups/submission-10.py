class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vocab = defaultdict(list)
        for word in strs:
            anagram = [0 for _ in range(26)]

            for charac in word:
                anagram[ord(charac) - ord('a')] += 1
            
            vocab[tuple(anagram)].append(word)
        
        res = []
        for value in vocab.values():
            res.append(value)
        return res