class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (len(nums) == 1):
            if nums[0] == target:
                return 0
            else:
                return -1
        
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            retVal = self.search(nums[mid:], target)
            if retVal == -1:
                return -1
            else:
                return mid + retVal