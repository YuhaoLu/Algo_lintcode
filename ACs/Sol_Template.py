"""
    0.Name: 
    

    1.Description:


    2.Example:

    2.1 Example 1:
        Input: 
        Output: 
        Explanation: 

    2.2 Example 2: 
        Input:
        Output:
        Explanation:

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
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            sign = -1
        x = x * sign
        while x > 0:
            digit = x % 10
            res = res * 10 + digit
            x = x // 10
        return sign * res if -2**31 <= res <= 2**31-1 else 0

if __name__ == '__main__':
    sol = Solution()
    x = 123
    sol.reverse(x)
