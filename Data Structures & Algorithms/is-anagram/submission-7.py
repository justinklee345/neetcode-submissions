class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocabOne = {}
        vocabTwo = {}

        for charac in s:
            vocabOne[charac] = vocabOne.get(charac, 0) + 1

        for charac in t:
            vocabTwo[charac] = vocabTwo.get(charac, 0) + 1
        
        return vocabOne == vocabTwo