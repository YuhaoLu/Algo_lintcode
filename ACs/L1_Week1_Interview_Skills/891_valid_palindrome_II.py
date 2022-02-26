"""
    0.Name: 
    Valid Palindrome II

    1.Description:
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

    2.Example:

    2.1 Example 1:
        Input: s = "aba"
        Output: true
        Explanation: Originally a palindrome.

    2.2 Example 2: 
        Input: s = "abca"
        Output: true
        Explanation: Delete 'b' or 'c'.

    2.3 Example 3:
        Input: s = "abc"   
        Output: false
        Explanation: Deleting any letter can not make it a palindrome.
    

    3.Solution:

    3.1 Solution 1:

        (a) Steps:

        (b) Corner Cases:

        (c) Complexity: Time - O(n), Space - O(1)
    
"""


import sys
sys.path.append('../.')
from lib_test import metatest

class Solution:
    def find_difference(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return start, end
            start += 1
            end -= 1
        return start, end

    def is_palindrome(self, s, start, end):
        start, end = self.find_difference(s, start, end)
        return start >= end
    
    @metatest
    def validPalindrome(self, s):
        if not s:
            return True

        # find the two pointers that encounters mismatch, ex. a b c d b a
        #                                                         ^ ^
        left, right = self.find_difference(s, 0, len(s) - 1)
        if left >= right:
            return True
        
        # check if delete one char will make the inner substr palindrome
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1) 

    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(s[left+1: right])
        return s[left + 1: right]


    @metatest # not good complexity, subsequence
    def longestPalindrome2(self, s: str) -> str:
        if not s:
            return s

        str_palindrome = ""
        for mid in range(len(s)):
            str_palindrome1 = self.get_palindrome_from(s, mid, mid)
            str_palindrome = str_palindrome1 if len(str_palindrome) < len(str_palindrome1) else str_palindrome
        
        length = len(str_palindrome)
        return str_palindrome[:length//2] + str_palindrome[length//2 + 1:]
if __name__ == '__main__':
    sol = Solution()
    s = "abca"
    sol.validPalindrome(s)
