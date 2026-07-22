class Solution:
    def climbStairs(self, n: int) -> int:
        mem = []

        for i in range(n+1):
            if i <= 1:
                mem.append(1)
                continue
            
            mem.append(mem[i-1] + mem[i-2])
        
        print(mem)
        return mem[-1]
        

        # to reach n, we just add the number of ways to reach n-1 and number of ways to reach n-2