class Solution:
    def reverseBits(self, n: int) -> int:

        bitsleft = 32
        res = 0
        while n:
            toadd = n & 1
            res = res << 1
            res = res | toadd
            n = n >> 1
            bitsleft -= 1
        res = res << bitsleft
        return res