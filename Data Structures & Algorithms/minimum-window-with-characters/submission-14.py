class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer, window = {}, {}

        for charac in t:
            answer[charac] = answer.get(charac, 0) + 1
        
        need, have = len(answer), 0

        minLen = float('inf')
        minStr = "" 

        l = 0
        for r in range(len(s)):
            charac = s[r]
            window[charac] = window.get(charac, 0) + 1
            if charac in answer and window[charac] == answer[charac]:
                have += 1
            # print("added", window, have, need)
            
            while have == need:
                # print(s[l : r + 1])
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minStr = s[l: r + 1]
                    # print("found", minLen,minStr)
                
                toremove = s[l]
                window[toremove] -= 1
                if toremove in answer and window[toremove] < answer[toremove]:
                    have -= 1
                l += 1
                # print("removed", window, have, need)
            
        return minStr