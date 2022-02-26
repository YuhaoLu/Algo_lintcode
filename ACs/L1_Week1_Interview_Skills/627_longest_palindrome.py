"""
    0.Name: 
    Longest Palindrome

    1.Description:
    Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
    This is case sensitive, for example "Aa" is not considered a palindrome here.

    2.Example:
    
    2.1 Example 1:
        Input : s = "abccccdd"
        Output : 7
        Explanation :
        One longest palindrome that can be built is "dccaccd", whose length is `7`.

    2.3 Constraints:
    

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
    @metatest
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        # Counter
        dict_char_count = {}
        for char in s:
            dict_char_count[char] = dict_char_count.get(char, 0) + 1
        res = 0
        for k in dict_char_count.values():
            if k % 2 == 0:
                res += k
            else:
                res += k - 1
        return res if res == len(s) else res + 1   


if __name__ == '__main__':
    sol = Solution()
    s = "abccccdd"
    sol.longestPalindrome(s)
