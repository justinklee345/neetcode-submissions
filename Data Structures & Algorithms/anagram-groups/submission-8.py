class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vocab = defaultdict(list)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for word in strs:
            freq = [0 for _ in range(26)]

            for letter in word:
                freq[ord(letter) - ord('a')] += 1


            vocab[tuple(freq)].append(word)
        
        return list(vocab.values())
                    