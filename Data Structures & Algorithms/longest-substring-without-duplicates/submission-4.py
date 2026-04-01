class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        longest = 0

        current = set()
        while r < len(s):
            print(current, l, r)
            if s[r] in current:
                longest = max(longest, len(current))
                while l <= r and s[r] in current:
                    current.remove(s[l])
                    l += 1
        
            current.add(s[r])
            r += 1
        

        return max(longest, len(current))
