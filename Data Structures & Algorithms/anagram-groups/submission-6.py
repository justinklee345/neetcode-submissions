class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def stringify(word):
            array = [0 for _ in range(26)]
            for charac in word:
                array[ord(charac) - ord('a')] += 1
            
            ret = ""
            for elem in array:
                ret += str(elem)
                ret += '|'
            
            return ret

        vocab = {}
        for word in strs:
            stringed = stringify(word)
            if stringed not in vocab:
                vocab[stringed] = [word]
            else:
                vocab[stringed].append(word)
        
        retVal = []
        for key, value in vocab.items():
            retVal.append(value)
        return retVal
            
