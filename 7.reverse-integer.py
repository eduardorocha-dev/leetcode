#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        output = str(abs(x))
        output = int(output[::-1])
        if x < 0: output = output * -1
        if output < -2**31 or output > 2**31 - 1: return 0
        return output

# range [-2**31, 2**31 - 1]

number = -123450
s = Solution()
print(s.reverse(number))

# @lc code=end

