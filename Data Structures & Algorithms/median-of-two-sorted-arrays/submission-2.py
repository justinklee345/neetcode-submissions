class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        median = -1
        while True:
            mA = (l + r) // 2
            mB = half - mA - 2

            leftA = A[mA] if mA >= 0 else float("-inf")
            rightA = A[mA + 1] if mA + 1 < len(A) else float("inf")
            leftB = B[mB] if mB >= 0 else float("-inf")
            rightB = B[mB + 1] if mB + 1 < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                #odd
                if total % 2 == 1:
                    return min(rightA, rightB)
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            
            elif leftA >= rightB:
                r = mA - 1
            else:
                l = mA + 1
            


