#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        low, high = 0, len(A)

        while low <= high:
            i = (low + high) // 2
            j = half - i

            print(f"A: {A[:i]} || {A[i:]}")
            print(f"B: {B[:j]} || {B[j:]}")

            Al = A[i-1] if i > 0 else float("-infinity")
            Ar = A[i] if i < len(A) else float("infinity")
            Bl = B[j-1] if j > 0 else float("-infinity")
            Br = B[j] if j < len(B) else float("infinity")

            if Al <= Br and Bl <= Ar:
                if total % 2:
                    return max(Al, Bl)
                else:
                    Lmax = max(Al, Bl)
                    Rmin = min(Ar, Br)
                    return (Lmax+Rmin)/2
                
            if Al > Br:
                high = high - 1
            else:
                low = low + 1


        return 0

s = Solution()


a1 = [1,2,3,8,9,10]
a2 = [4,5,6,7,8,11]

b1 = [1,2,3]
b2 = [6,7,8,9,10]




a = s.findMedianSortedArrays(b1, b2)
print(a)
# @lc code=end

