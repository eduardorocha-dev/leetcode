#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        size = 0

        for right, char in enumerate(s):
            if char in map and map[char] >= left:
                left = map[char] + 1
            map[char] = right
            if right - left >= size:
                size = right - left
            print(f"Iteration: {right}, Char:{char}, Size: {size}")
        return size


s = Solution()
string = "abcdefaaaaaaabc"
v = s.lengthOfLongestSubstring(string)
print(f"Output: {v}")
# @lc code=end

