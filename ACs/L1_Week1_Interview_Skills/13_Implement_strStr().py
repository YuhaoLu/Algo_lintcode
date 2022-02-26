"""
    0.Name: 
    Strstr

    1.Description:
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.
    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

    2.Example:

    2.1 Example 1:
        Input: haystack = "hello", needle = "ll"
        Output: 2

    2.2 Example 2:
        Input: haystack = "aaaaa", needle = "bba"
        Output: -1
    
    2.3 Example 3:
        Input: haystack = "", needle = ""
        Output: 0

    2.3 Constraints:
        0 <= haystack.length, needle.length <= 5 * 104
        haystack and needle consist of only lower-case English characters.

    3.Solution:
    3.1 Solution 1(Bruteforce):
        (a) Steps:
        hello 
        ll
         ll
          ll
        m = 5
        n = 2 
        for i in range(m-n+1)
        (b) Corner Cases: 
        

        (c) Complexity: Time - O(m * n), Space - O(1)

    3.2 Solution 2(Robin Karp):
        (a) Steps:
            Compare the hashCode of a word in haystack and target needle
            If the hashCode[word] == hashCode[needle], it's very likely the two words match,
            but if any hash collisions happen, just double check the extracted word with target needle. 

            To make the algorthm faster, caculate the hash by only using the previous results and one char's weight
            haystack: a b c d e f
            needle: c d e
                            c    d    e
            hash_needle:   'c' * 31^2 + 'd' * 31 + 'e'
                            a    b    c
            hash_word:     'a' * 31^2 + 'b' * 31 + 'c'
                                 b    c    d 
                            a    b    c  + d - a
            hash_next_word: ((hash_word * 31 + 'd') - 'a' * 31^3) % BASE
            
        (c) Complexity: Time - O(m + n), Space - O(1)

    3.3 Solution 3:
        (a) Steps:
            The KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than once in the pattern) of the pattern and improves the worst case complexity to O(n). 
            The basic idea is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. 
            We take advantage of this information to avoid matching the characters that we know will anyway match. 
            aaaaabaaaba
            ||||
            aaaa

            Bruteforce:
            aaaaabaaaba
            ||||
            aaaa

            KMP:
            aaaaabaaaba
                |
            aaaa
            
                
            (1) Create a longest proper prefix which is also suffix
                a a a a a b a a a b a
                0 1 2 3 4 0 1 2 3 0 1

                a a a a a b a a a b a
                i
                j
                a a a a a b a a a b a
                    i
                j
                a a a a a b a a a b a
                    i
                    j
                a a a a a b a a a b a
                        i
                    j
                a a a a a b a a a b a
                        i
                        j
                a a a a a b a a a b a
                            i
                j
            (2) Search 

        (b) Corner Cases: 
        

        (c) Complexity: Time - O(m + n), Space - O(n)

        Reference: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
    4.Summary

    
    
"""

import sys
sys.path.append('../.')
from lib_test import metatest

from typing import List


class Solution:
    @metatest
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0

        # Note: range(0) = []
        # if m < n:
        #     return -1
        res = -1
        for i in range(m-n+1):

            # if haystack[i:i+n] == needle:
            #     res = i
            #     break

            # for ... else ...
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
            else: 
                res = i
        return res

    @metatest
    def strStr2(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        
        BASE = 2 ** 20
        power = 1
        for i in range(n):
            power = (power * 31) % BASE
        
        hash_needle = 0 
        for i in range(n):
            hash_needle = (hash_needle * 31 + ord(haystack[i])) % BASE

        hash_word = 0
        for i in range(m):
            # abc + d
            hash_word = (hash_word * 31 + ord(haystack[i])) % BASE
            if i < m - 1:
                continue

            # abcd - a
            if i >= m:
                hash_word = hash_word - ord(haystack[i - m] * power) % BASE
                hash_word = hash_word + BASE if hash_word < 0 else hash_word
            
            # double check the string 
            if hash_word == hash_needle:
                if haystack[i: i+m] == needle:
                    return i
        return -1

    def KMPSearch(self, pat, txt):
        def BuildLPSList(pat):
            m = len(pat)
            lps = [0] # lps[0] is always 0
            j = 0     # length of the previous longest prefix suffix
        
            # the loop calculates lps[i] for i = 1 to M-1
            for i in range(1, m):
                if pat[i]== pat[j]:
                    lps.append(j+1)
                    i += 1
                    j += 1
                else:
                    # ???
                    if j != 0:
                        j = lps[j-1]
                        # note that we do not increment i here
                    else:
                        lps.append(0)
                        i += 1
            return lps
        m, n = len(pat), len(txt)

        # create lps[] that will hold the longest prefix suffix 
        # values for pattern
        j = 0 # index for pat[]
    
        # Preprocess the pattern (calculate lps[] array)
        lps = BuildLPSList(pat )
    
        i = 0 # index for txt[]
        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
    
            if j == m:
                print ("Found pattern at index " + str(i-j))
                j = lps[j-1]
    
            # mismatch after j matches
            elif i < n and pat[j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
  
    

if __name__ == '__main__':
    sol = Solution()
    haystack = "hello"
    needle = "ll"
    res = sol.strStr(haystack, needle)
    res = sol.KMPSearch(haystack, needle)
