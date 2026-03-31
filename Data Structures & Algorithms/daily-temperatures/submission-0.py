class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if len(stack) == 0:
                stack.append((temperatures[i], i))
                continue
            
            result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        
        return result


                
"""


30 38 30 36 35 40 28
0  0  0  0  1  0  0


stack



38 1
30 2
36 3
40 5

"""