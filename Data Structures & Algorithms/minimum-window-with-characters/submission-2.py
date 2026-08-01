class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        answer, window = {}, {}

        for c in t:
            answer[c] = answer.get(c, 0) + 1
        
        shortest, shortestLen= "", float("inf")
        have, need = 0, len(answer)

        l = 0
        for r in range(len(s)):
            charac = s[r]
            window[charac] = window.get(charac, 0) + 1
            if charac in answer and window[charac] == answer[charac]:
                have += 1
            
            while have == need:
                # print(window, answer, s[l : r + 1], shortest, have)
                if r - l < shortestLen:
                    shortestLen = r - l
                    shortest = s[l : r + 1]

                toRemove = s[l]
                window[toRemove] -= 1
                if toRemove in answer and window[toRemove] < answer[toRemove]:
                    have -= 1
                l += 1
        
        return shortest
