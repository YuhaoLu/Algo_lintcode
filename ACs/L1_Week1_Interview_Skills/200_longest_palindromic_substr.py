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
    3.1 Solution 2:
        3.1.1 Steps:
        abba
        racecar

        Suppose the middle elem start from i, Check the two cases across the list

    
        3.1.2 Corner Cases: 
        nums.length < 2

        3.1.3 Complexity: Time - O(n), Space - O(1)

    4.Summary

    
    
"""

import sys
sys.path.append('../.')
from lib_test import metatest

from typing import List, Tuple
class Solution:
    @metatest
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            length1 = self.expandAroundCenter(s, i, i)
            length2 = self.expandAroundCenter(s, i, i + 1)
            length = max(length1, length2)
            if length > end - start:
                start = int(i - (length - 1) / 2)
                end = int(i + length // 2)
        return s[start:end + 1]

    def expandAroundCenter(self, s:str, i: int, j: int) -> int:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1

    @metatest
    def longestPalindrome2(self, s: str) -> str:
				#init table
        table = [[0 for x in range(len(s))] for x in range(len(s))]
        longest_index = [0,0]
        longest_len = 1
        for i in range(len(s)):
            table[i][i] = 1
				#fill the table in diagnal fashion
        for i in range(0,len(s)):
            for front in range(0,len(s)-1-i):
                back = front + i+1
                if s[front] == s[back]:
										#handle base case when len is two
                    if back-front+1 == 2:
                        table[front][back] = 2
										#check if subseq is a palindrome 
                    elif table[front+1][back-1]!=0:
                        table[front][back] = table[front+1][back-1] + 2
										#check if cur palindrome is longest
                    if longest_len < table[front][back]:
                        longest_index=[front,back]
                        longest_len = back-front+1
                else:
                    table[front][back] = 0
        return s[longest_index[0]:longest_index[1]+1]

if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    sol.longestPalindrome(s)