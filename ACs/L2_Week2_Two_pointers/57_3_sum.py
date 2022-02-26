"""
    0.Name: 
    3Sum

    1.Description:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    2.Example:

    2.1 Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]

    2.2 Example 2:
        Input: nums = []
        Output: []

    2.3 Example 3:
        Input: nums = [0]
        Output: []

    2.4 Constraints:
        0 <= nums.length <= 3000
        -105 <= nums[i] <= 105

    3.Solution:
    3.1 Solution 1:
        3.1.1 Steps:
        ----------------------
        | 1 | 1 | 2 | ...
        ----------------------
        i   
        j
        
        i - next location to store
        j - iterate through to find unique items
        
        Use Array as a Linklist ???
    
        3.1.2 Corner Cases: 
        nums.length < 2

        3.1.3 Complexity: Time - O(n), Space - O(1)

    4.Summary

    
    
"""

from runpy import run_module
import sys
from unittest import result
sys.path.append('../../../0_Template/')
from lib_test import metatest

from typing import List, Tuple
class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(self.nums) - 1
        while left < right:
            li_res = []
            # 去重： 如果左指针当前数字跟左边数字相同，左指针向中间移动，跳过重复
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            # 去重： 如果右指针当前数字跟右边数字相同，右指针向中间移动，跳过重复
            while left < right and nums[right] == nums[right + 1]:
                right -= 1

            two_sum = self.nums[left] + self.nums[right]
            if two_sum == target:
                li_res.append([-target, nums[left], nums[right]])
            elif two_sum < target:
                left += 1
            else:
                right -= 1

        return li_res
        
    @metatest
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        li_res = []
        # Note: input validation!
        if not nums or len(nums) < 3:
            return li_res
        
        nums = sorted(nums)
        # print(nums)

        for i in range(len(nums-2)): # optimization: len_nums - 2
            # 去重: 如果当前元素和左边元素一样，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            results = self.twoSum2(nums[i+1:], 0 - nums[i])
            li_res.extend(results)
        return li_res
            

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    sol.threeSum(nums)