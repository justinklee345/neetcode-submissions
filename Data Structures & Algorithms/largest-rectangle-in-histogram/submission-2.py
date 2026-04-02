class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftWall = [0 for i in range(len(heights))]
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                leftWall[i] = stack[-1] + 1
            stack.append(i)

        rightWall = [len(heights) - 1 for i in range(len(heights))]
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                rightWall[i] = stack[-1] - 1
            stack.append(i)

        print(leftWall, "\n", rightWall)

        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i] * (rightWall[i] - leftWall[i] + 1))
        return maxArea


"""
1 4 3 2
0 1 1 1

7 1 7 2 2 4


0 0 1 1 1 4
1 0 3 0 0 0
should be:
0 0 2 2 2 5
0 5 2 5 5 5
list:
0 0 0 0 1 0

stack:
1


2
1
del 0

if the stack is empty we just push and continue

while the stack is not empty and the current height is less than the stack's top element's height:
    we just keep 


"""