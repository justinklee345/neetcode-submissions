class Solution:
    def numDecodings(self, s: str) -> int:
        """
        dec[i] represents the number of ways to decode a string of length i
        dec[i] = 
        dec[3] = 
        dec[2] = dec[0] if s[i-1] + s[i] <= 26 and s[i-1] != 0 else 0 + dec[1] if s[i-1] != 0
        dec[1] = 0 if s[i] == 0 else 1
        dec[0] = 1

        """
        dec = [1]

        for i in range(len(s)):
            if i == 0:
                if int(s[i]) == 0:
                    dec.append(0)
                else:
                    dec.append(1)
                continue
            
            val = 0
            two = int(s[i-1] + s[i])
            one = int(s[i])
            if two >= 10 and two <=26:
                val += dec[-2]
            
            if one != 0:
                val += dec[-1]
            dec.append(val)
        print(dec)
        return dec[-1]

