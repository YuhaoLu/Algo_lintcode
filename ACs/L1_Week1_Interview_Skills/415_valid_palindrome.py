"""
    0.Name: 
    Valid Palindrome

    1.Description:
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    2.Example:
    
    2.1 Example 1:
        Input: "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama"
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
    # is_* , has_*
    def is_valid(self, char):
        return char.isdigit() or char.isalpha()

    @metatest
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            # skip invalid char on the left
            while left < right and not self.is_valid(s[left]):
                left += 1
            # skip invalid char on the right
            while left < right and not self.is_valid(s[right]):
                right -= 1
            # if left != right: return False
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True  

if __name__ == '__main__':
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    sol.isPalindrome(s)
