class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def findPalindrome(left: int, right:int) -> str:
            while left >= 0 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""

        for i in range(len(s)):

            current_palindrome = findPalindrome(i, i)
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome

            current_palindrome = findPalindrome(i, i + 1)
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome

        return longest_palindrome