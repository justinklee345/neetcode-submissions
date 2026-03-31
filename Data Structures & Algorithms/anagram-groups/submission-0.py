class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = {}

        for word in strs:
            s_word = "".join(sorted(word))
            if s_word in a_map.keys():
                a_map[s_word].append(word)
            else:
                a_map[s_word] = [word]
        
        retList = []
        for values in a_map.values():
            retList.append(values)
        return retList