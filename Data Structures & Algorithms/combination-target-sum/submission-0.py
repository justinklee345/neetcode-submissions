class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start_index, current_path, current_sum):
            if current_sum == target:
                res.append(current_path[:])
        
            for i in range(start_index, len(nums)):
                if nums[i] + current_sum > target:
                    continue
                
                current_path.append(nums[i])

                backtrack(i, current_path, current_sum + nums[i])

                current_path.pop()
            
        backtrack(0, [], 0)
        return res