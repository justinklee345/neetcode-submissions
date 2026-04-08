class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        current_max = -1

        for ele in height:
            current_max = max(current_max, ele)
            left_max.append(current_max)

        current_max = -1
        for i in range(len(height) - 1, -1, -1):
            current_max = max(current_max, height[i])
            right_max.append(current_max)
        right_max = right_max[::-1]

        print(left_max)
        print(right_max)

        area = 0
        for i in range(len(height)):
            area += min(left_max[i], right_max[i]) - height[i]
                
        return area

