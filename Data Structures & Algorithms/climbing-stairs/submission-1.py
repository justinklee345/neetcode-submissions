class Solution:
    def climbStairs(self, n: int) -> int:
        """
        climb[i] represents the number of ways to reach the ith staircase
        climb[i] = climb[i-1] + climb[i-2]
        climb[0] = 1
        climb[1] = 1


        """

        climb = []
        for i in range(n+1):
            if i <= 1:
                climb.append(1)
                continue
            
            climb.append(climb[i-1] + climb[i-2])
        
        print(climb)
        return climb[-1]