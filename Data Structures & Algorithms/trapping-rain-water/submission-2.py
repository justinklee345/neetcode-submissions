class Solution:
    def trap(self, height: List[int]) -> int:
        right = [0 for _ in range(len(height))]
        leftCol = 0
        for i, h in enumerate(height):
            leftCol = max(leftCol, h)
            right[i] = leftCol
        
        left = [0 for _ in range(len(height))]
        rightCol = 0

        for i in range(len(height) - 1, -1, -1):
            rightCol = max(rightCol, height[i])
            left[i] = rightCol

        
        res = 0
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]

        return res




'''


0 2 0 3 1 0 1 3 2 1
0 0 2 0 3 3 3 0 3 3
3 3 3 0 3 3 3 0 0 0

0 0 2 0 3 3 3 0 0 0 


'''