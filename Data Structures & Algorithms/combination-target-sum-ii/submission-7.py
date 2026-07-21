class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start_idx, current_path, current_sum):
            if current_sum == target:
                res.append(current_path[:])
                return
            
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i-1]:
                    continue
                
                if current_sum + candidates[i] > target:
                    return
                
                current_path.append(candidates[i])
                backtrack(i+1, current_path, current_sum + candidates[i])
                current_path.pop()
        
        backtrack(0, [], 0)
        return res