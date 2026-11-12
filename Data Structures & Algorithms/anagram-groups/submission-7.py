class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vocab = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for word in strs:
            freq = [0 for _ in range(26)]
            key = ""

            for letter in word:
                freq[ord(letter) - ord('a')] += 1

            for idx, cnt in enumerate(freq):
                if cnt > 0:
                    key += alphabet[idx] + str(cnt)
            
            if key in vocab:
                vocab[key].append(word)
            else:
                vocab[key] = [word]
        
        retVal = []
        for key, value in vocab.items():
            retVal.append(value)
        return retVal
                    