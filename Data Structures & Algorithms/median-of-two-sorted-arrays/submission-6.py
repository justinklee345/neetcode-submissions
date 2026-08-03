class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        total = len(B) + len(A)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            mA = (l + r) // 2
            mB = half - mA - 2
            print(l, r, mA, mB)

            aleft = A[mA] if mA >= 0 else float('-inf')
            aright = A[mA + 1] if mA + 1 < len(A) else float('inf')
            bleft = B[mB] if mB >= 0 else float('-inf')
            bright = B[mB + 1] if mB + 1 < len(B) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2 == 1:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft >= bright:
                r = mA - 1
            else:
                l = mA + 1


'''
1 2 3 4 5 6 7 8
1 2 3 4 5

1 1 2 2 3 3 | 4 | 4 5 5 6 7 8

l       r
m = 3
'''