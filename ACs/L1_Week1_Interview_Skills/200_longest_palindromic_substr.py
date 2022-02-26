"""
    0.Name: 
    Longest Palindromic Substring

    1.Description:
    Given a string s, return the longest palindromic substring in s.

    2.Example:

    2.1 Example 1:
        Input: s = "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.

    2.2 Example 2:
        Input: s = "cbbd"
        Output: "bb"

    2.3 Example 3:
        Input: s = "a"
        Output: "a"

    2.4 Example 4:
        Input: s = "ac"
        Output: "a"
        
    2.5 Constraints:
        1 <= s.length <= 1000
        s consist of only digits and English letters.

    3.Solution:
        3.1 Solution 1(Bruteforce):
            (a) Steps:
            abba
            racecar

            for 起点 O(n)
                for 终点 O(n)
                    is_palindromic(s[起点，终点])

        
            (b) Corner Cases: 
            nums.length < 2

            (c) Complexity: Time - O(n^3), Space - O(1)

        3.2 Solution 2(Middle out):
            (a) Steps:
            abba
            racecar

            Suppose the middle elem start from i, Check the two cases across the list

        
            (b) Corner Cases: 
            nums.length < 2

            (c) Complexity: Time - O(n^2), Space - O(1)
        
        3.3 Solution 3(Dynamic Programming):
            (a) Steps:
            abba
            racecar

            区间型动态规划
            is_palindrome[i][j] = is_palindrome[i+1][j-1]) && s[i] == s[j]

        
            (b) Corner Cases: 
            nums.length < 2

            (c) Complexity: Time - O(n^2), Space - O(n^2)
        
        3.4 Solution 4(Manacher's Algorithm):
            (a) Steps:
            abba
            racecar

        
            (b) Corner Cases: 
            nums.length < 2

            (c) Complexity: Time - O(n), Space - O(1)
    4.Summary

    
    
"""

import sys
sys.path.append('../.')
from lib_test import metatest
from pprint import pprint

from typing import List, Tuple
class Solution:
    # Solution 1
    def is_palindrome(self, s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return left >= right

    @metatest
    def longestPalindrome(self, s: str) -> str:
        # 输入异常检测
        if s is None:
            return None
        
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                if self.is_palindrome(s, i, i + length -1):
                    return s[i: i+length]
        return ""

    # Solution 2
    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(s[left+1: right])
        return s[left + 1: right]


    @metatest
    def longestPalindrome2(self, s: str) -> str:
        if not s:
            return s

        str_palindrome = ""
        for mid in range(len(s)):
            # a b a
            str_palindrome1 = self.get_palindrome_from(s, mid, mid)
            # a b b a
            str_palindrome2 = self.get_palindrome_from(s, mid, mid + 1)
            str_palindrome = str_palindrome1 if len(str_palindrome) < len(str_palindrome1) else str_palindrome
            str_palindrome = str_palindrome2 if len(str_palindrome) < len(str_palindrome2) else str_palindrome

        return str_palindrome

    # Solution 3
    @metatest
    def longestPalindrome3(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        
        for i in range(1, n):
            is_palindrome[i][i-1] = True # ???????
        pprint(is_palindrome)
        
        start, longest = 0, 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
                longest = length
                start = i
            return s[start: start + longest]

if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    sol.longestPalindrome(s)
    sol.longestPalindrome2(s)
    sol.longestPalindrome3(s)