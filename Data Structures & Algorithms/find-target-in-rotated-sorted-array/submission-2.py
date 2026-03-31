class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            print(l, r)
            if l == r and nums[l] != target:
                return -1
        
            m = l + ((r-l) // 2)

            mVal, rVal = nums[m], nums[r]

            if mVal == target:
                return m
            if rVal == target:
                return r
        

            if mVal > rVal > target:
                l = m + 1
            elif mVal > target > rVal:
                r = m
            elif rVal > mVal > target:
                r = m
            elif rVal > target > mVal:
                l = m + 1
            elif target > mVal > rVal:
                l = m + 1
            elif target > rVal > mVal:
                r = m

        return nums[l] or -1
"""



3 5 6 0 1 2 (target = 4)
3 5 (target = )

1 3 (target = 3)
1 3 (m = 1 r = 3 t= 3)



4 5 6 7 8 1 2 3  target=2
4 5 6 7 8 1 2 3 (7 3) m > r > t, look right
8 1 2 3 (1 3) r > t > m, look right

t > m > r 
45678123 (target = 8) (7 3)
t > r > m
81234567 (tgarget = 8) (3 7)

2 3

r > m > t
1 2 3 4 5 6 7 8 (4, 8) target = 2 r > m > t


4 5 6 7 8 1 2 3  target=5
4 5 6 7 8 1 2 3 (7 3) m > t > r, look left


4 5 6 (5 6) 

4 5 6 7 8 1 2 3  target=8
4 5 6 7 8 1 2 3 (7 3) target t > m > r, look right
4 5 6 (5 6) 



"""