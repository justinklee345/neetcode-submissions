class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        answer, window = {}, {}

        for charac in t:
            answer[charac] = answer.get(charac, 0) + 1
        
        have, need = 0, len(answer)
        shortest, shortestLen = "", float('inf')

        l = 0
        for r in range(len(s)):
            charac = s[r]
            window[charac] = window.get(charac, 0) + 1

            if charac in answer and window[charac] == answer[charac]:
                have += 1

            while have == need:
                if r - l + 1 < shortestLen:
                    shortest = s[l : r + 1]
                    shortestLen = r - l + 1    
                
                toremove = s[l]
                window[toremove] -= 1

                if toremove in answer and window[toremove] < answer[toremove]:
                    have -= 1
                l += 1
        return shortest
         