class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp
        # canjump[i] refers to 
        canJump = [False for _ in range(len(nums))]
        canJump[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i]
            for j in range(jump + 1):
                if i + j < len(nums) and canJump[i + j]:
                    print("HI??")
                    canJump[i] = True
                    break
            
        print(canJump)
        return canJump[0]


