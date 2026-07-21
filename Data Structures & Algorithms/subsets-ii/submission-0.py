class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start_idx, current_path):
            res.append(current_path[:])

            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i-1]:
                    continue
                
                current_path.append(nums[i])
                backtrack(i+1, current_path)
                current_path.pop()
            
        backtrack(0, [])
        return res