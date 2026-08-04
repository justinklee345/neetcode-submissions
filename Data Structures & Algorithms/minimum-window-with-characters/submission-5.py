class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t == "": return ""
        answer, window = {}, {}

        for charac in t:
            answer[charac] = answer.get(charac, 0) + 1
        
        have, need = 0, len(answer)
        l = 0
        shortest, shortestLen = "", float('inf')
        for r in range(len(s)):
            toAdd = s[r]
            window[toAdd] = window.get(toAdd, 0) + 1
            if toAdd in answer and window[toAdd] == answer[toAdd]:
                have += 1
            
            while have == need:
                if r - l < shortestLen:
                    shortestLen = r - l
                    shortest = s[l : r + 1]
                toRemove = s[l]
                window[toRemove] = window.get(toRemove, 0) - 1
                l += 1
                if toRemove in answer and window[toRemove] < answer[toRemove]:
                    have -= 1
        return shortest