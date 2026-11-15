class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        answer = {}
        for charac in t:
            answer[charac] = answer.get(charac, 0) + 1
        print(answer)

        have, need = 0, len(answer)
        res, resLength = "", float('inf')

        vocab = {}
        
        l = 0
        for r in range(len(s)):
            curr = s[r]
            vocab[curr] = vocab.get(curr, 0) + 1

            if curr not in answer:
                # print('first', vocab)
                continue
            
            if vocab[curr] != answer[curr]:
                # print('second', vocab[charac], answer[charac])
                continue
            
            
            have += 1
            print(vocab)
            while have == need:
                # store found substring
                # print("valid: ", s[l : r + 1], vocab)
                if r - l + 1 < resLength:
                    
                    res = s[l : r + 1]
                    resLength = r - l + 1

                # print(l, r)
                removed = s[l]
                vocab[removed] -= 1
                l += 1
                if removed in answer and answer[removed] > vocab[removed]:
                    have -= 1
        return res
                





        