#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or  numRows == 1: return s

        matrix = [ [] for i in range(numRows)]
        
        row_index = 0
        direction = -1

        for char in s:
            row = matrix[row_index]
            row.append(char)

            if row_index >= numRows - 1 or row_index <= 0:     
                direction = direction * (-1)
                
            row_index = row_index + direction         
        
        return "".join(["".join(row) for row in matrix])



Input = "PAYPALISHIRING"
numRows = 3
Output= "PAHNAPLSIIGYIR"


s = Solution()
out = s.convert(s=Input, numRows=numRows)
print(out)
"""
P   A   H   N
A P L S I I G
Y   I   R
"""

# @lc code=end

