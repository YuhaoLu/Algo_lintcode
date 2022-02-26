"""
    0.Name: 
    Two Sum III

    1.Description:
    Design and implement a TwoSum class. It should support the following operations: add and find.

    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.

    2.Example:

    2.1 Example 1:
        add(1); add(3); add(5);
        find(4) // return true
        find(7) // return false

    3.Solution:
    Time Complexity:                                add     find
    Sol1:Sorted List + Encountering 2 pointers      O(N)    O(N)
    Sol2:Hashmap                                    O(1)    O(N)

    3.1 Solution 1(Hash Counter):
        (a) Steps:
            1. Iterate through nums list and save each appeared num in a hashset as {num: index}
                ----------------------
                | 2 | 7 | 11 | 15 |...
                ----------------------
                {2:0, 7:1 ...}
            2. Check whether the difference(target- num) is in the hashset
                If yes, return the index of the number pair 
                If no, update the num list hashset
    
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

        (c) Complexity: Time - O(n), O(1) - if the list of nums is sorted

    4.Summary

    
    
"""

import sys

from numpy import number
sys.path.append('../.')
from lib_test import metatest

from typing import List, Tuple, Dict
class TwoSum2:
    def __init__(self) -> None:
        self.dict_counter_num = {}
    
    # Add to the hash Counter
    def add(self, num:int) -> Dict[int, int]:
        self.dict_counter_num[num] = self.dict_counter_num.get(num, 0) + 1

    # find two sum with Hashmap
    def find(self, target:int) -> List[int]:
        for num1 in self.dict_counter_num:
            num2 = target - num1
            cnt_num2 = 2 if (num1 == num2) else 1
            if self.dict_counter_num.get(num2) >= cnt_num2:
                return [num1, num2]
        return [-1, -1]

class TwoSum:
    def __init__(self) -> None:
        self.nums = []
    
    # Insertion Sort
    def add(self, num:int) -> List[int]:
        self.nums.append(num)
        index = len[self.nums] - 1
        while(index > 0) and self.nums[index - 1] > self.nums[index]:
            # swap nums[index - 1] <-> nums[index]
            self.nums[index], self.nums[index - 1] = self.nums[index - 1], self.nums[index] 
            index -= 1
        return self.nums

    # find two sum with two pointers
    def find(self, target:int) -> List[int]:
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                return [left, right]
        return [-1, -1]


    

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    sol.twoSum2(nums, target)