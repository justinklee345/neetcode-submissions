class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            other = target - nums[i]
            if other in map.keys():
                return [map[other], i]
            map[nums[i]] = i