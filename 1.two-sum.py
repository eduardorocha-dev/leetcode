#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in dict:
                print(f"Match: nums[{i}] = {nums[i]}, nums[{dict[complement]}] = {nums[ dict[complement] ]}")
                return [i, dict[complement]]
            dict[n] = i


array: list[int] = [1, 3, 5, 8, 13, 21]
target: int = 34
s = Solution()
s.twoSum(nums=array, target=target)

# @lc code=end

