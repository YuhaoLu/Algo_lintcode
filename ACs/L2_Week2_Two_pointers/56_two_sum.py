"""
    0.Name: 
    Two Sum

    1.Description:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    2.Example:

    2.1 Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    2.2 Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

    2.3 Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]

    2.4 Constraints:
        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.

    3.Solution:
    3.1 Solution 1(Hashmap Counter):
        (a) Steps:
            1. Iterate through nums list and save each appeared num in a hashmap as {num: index}
                ----------------------
                | 2 | 7 | 11 | 15 |...
                ----------------------
                {2:0, 7:1 ...}
            2. Check whether the difference(target- num) is in the hashsmap
                If yes, return the index of the number pair 
                If no, update the num list hashmap
    
        (b) Corner Cases: 
        nums.length < 2

        (c) Complexity: Time - O(n), Space - O(n)
    3.2 Solution 2 (Encountering 2 pointers - sorted list):
        (a) Steps:
            1. Sort the list if the list hasn't been sorted
                ----------------------
                | 2 | 7 | 11 | 15 |...
                ----------------------
            2. set two pointers (left, right) to the head and tail of the number list
                ----------------------
                | 2 | 7 | 11 | 15 |...
                ----------------------
                  ^             ^
                 left         right
                if nums[left] + num[right] < target:
                    move left pointer to right 
                if nums [left] + num[right] > target:
                    move right pointer to left
                Proof:
                    The pointer movements can cover all the possible number pair combination 
                    start from sum[head + tail]
                    and change the sum 1 step larger(or less) by moving the pointers
        (b) Corner Cases: 
        nums.length < 2

        (c) Complexity: Time - O(nlogn), Space - O(n)
                               O(n), O(1) - if the list of nums is sorted

    4.Summary

    
    
"""

import sys

from numpy import number
sys.path.append('../.')
from lib_test import metatest

from typing import List, Tuple
class Solution:
    @metatest
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
    @metatest
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        dict_num_index = {}
        for i in range(len(nums)):
            if target - nums[i] in dict_num_index:
                return [dict_num_index[target-nums[i]], i]
            else:
                dict_num_index[nums[i]] = i
        return [-1, -1]

    @metatest
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        li_sort_nums = [(num, index) for index, num in enumerate(nums)]
        li_sort_nums.sort()

        left = 0 
        right = len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                return sorted([nums[left][1], nums[right][1]])
        return [-1, -1]

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    sol.twoSum2(nums, target)