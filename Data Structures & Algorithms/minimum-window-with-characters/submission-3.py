class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        answer, window = {}, {}
        for charac in t:
            answer[charac] = answer.get(charac, 0) + 1
        
        have, need = 0, len(answer)
        l = 0
        shortest, shortestLen = "", float("inf")

        for r in range(len(s)):
            print(have, need, window)
            charac = s[r]
            window[charac] = window.get(charac, 0) + 1
            if charac in answer and window[charac] == answer[charac]:
                have += 1
            
            while have == need:
                if r - l < shortestLen:
                    shortest = s[l: r + 1]
                    shortestLen = r - l
                    print(shortest, shortestLen)

                toRemove = s[l]
                window[toRemove] -= 1
                if toRemove in answer and window[toRemove] < answer[toRemove]:
                    have -= 1
                l += 1
            
        return shortest