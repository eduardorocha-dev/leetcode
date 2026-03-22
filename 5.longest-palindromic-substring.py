#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        local_max = 0
        positions = [0,0]
        for i in range(len(s)):
            len1, l1, r1 = self.palindrome_around_positions(i, i, s)
            len2, l2, r2 = self.palindrome_around_positions(i, i+1, s)
            
            if len1 > local_max:
                local_max = len1
                positions[0] = l1
                positions[1] = r1
            
            if len2 > local_max:
                local_max = len2
                positions[0] = l2
                positions[1] = r2
            
        if local_max > 0:
            return s[positions[0]: positions[1] + 1]
        else:
            return ""

    def palindrome_around_positions(self, left: int, right: int, s: str):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return right - left - 1, left + 1, right - 1





s = Solution()

target = "babada"

a = s.longestPalindrome(target)
print(a)
# @lc code=end

